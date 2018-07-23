# -*- coding:UTF-8 -*-
import os
import requests
import time
import re
from bs4 import BeautifulSoup


def extract(content):
    sub_sub_dirs = []
    sub_sub_files = []
    # todo bs -> fileList
    soup = BeautifulSoup(content, "html.parser")
    sources = soup.findAll('tr', attrs={'class': 'js-navigation-item'})
    for source in sources:
        isBack = source.find('a', attrs={'rel': 'nofollow'})
        if isBack:
            continue
        a = source.find('svg', attrs={'class': 'octicon octicon-file-directory'})
        url = 'https://github.com' + source.find('a', attrs={'class': 'js-navigation-open'}).get('href')
        if a is None:
            #  isFile
            sub_sub_files.append(url)
        else:
            # is directory
            sub_sub_dirs.append(url)

    return sub_sub_dirs, sub_sub_files


def recursive(prev_url, sub_dirs, sub_files):
    for file in sub_files:
        if file == 'pom.xml':
            flag = 'maven'
            return
        if file == 'build.gradle':
            flag = 'gradle'
            return
        if file == 'androidmanifest.xml':
            flag = 'android'
            return
    for dir in sub_dirs:
        url = prev_url + '/' + dir
        req = requests.get(url)
        content = req.text
        sub_sub_dirs, sub_sub_files = extract(content)
        flag = recursive(url, sub_sub_dirs, sub_sub_files)
        if flag == 'maven' or flag == 'gradle' or flag == 'android':
            return flag
    return 'none'


def crawler():
    path = os.getcwd()
    m_list = []
    cache = path + '/500gt/'
    with open(path + '/starsmt500.csv', 'r', encoding='utf-8') as f:
        flag = True
        for line in f:
            if flag:
                flag = False
                continue
            data = line.split(',')
            url = data[2]
            m_list.append(url)

    cnt = 0
    for url in m_list:
        name = url.split('/')
        print(name[-1])
        print(url + '/tree/master')
        req = requests.get(url + '/tree/master')
        req.encoding = 'utf-8'
        print(req.text)
        sub_dirs, sub_files = extract(req.text)
        flag = recursive(url + '/tree/master', sub_dirs, sub_files)
        if flag == 'maven' or flag == 'gradle':
            cnt += 1
        print(flag)
        break
    print(len(m_list))
    print(cnt)
    # print(text)
    # with open(cache+name[-1]+".html",'wb') as f:
    # f.write(content)
    # time.sleep(3)


# crawler()
req = requests.get('https://github.com/hangum/TadpoleForDBTools/tree/master/com.hangum.tadpole.application.initialize.core')
req.encoding = 'utf-8'
a, b = extract(req.text)
print(a, b)
