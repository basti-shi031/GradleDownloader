#-*- coding:UTF-8 -*- 
import os
import requests
import time
import re
from bs4 import BeautifulSoup
from queue import Queue
import sys
# input star_gt_500.csv output I-result

def checkFile(sub_files):
    for file1 in sub_files:
        file = file1.lower()
        if file.endswith('pom.xml'):
            return 'maven'
        if file.endswith('build.gradle'):
            return 'gradle'
        if file.endswith('androidmanifest.xml'):
            return 'android'
    return 'No'
def extract(path,items):
    dirs = []
    files = []
    for item in items:
        abs_path = path+'/'+item
        if os.path.isdir(abs_path):
            dirs.append(abs_path)
        else:
            files.append(abs_path)
    return dirs,files

def checkOneProj(path):
    queue = Queue()
    queue.put(path)
    m_flag = set()
    while queue.qsize() !=0 :
        q_path = queue.get()
        items = os.listdir(q_path)
        sub_dirs, sub_files  = extract(q_path,items)
        flag = checkFile(sub_files)
        if flag =='maven' or flag =='gradle':
            m_flag.add(flag)
        if flag =='android':
            m_flag.add(flag)
            break
        for dir in sub_dirs:
            queue.put(dir)
    return m_flag

def run():
    path = os.getcwd()
    m_list = []
    
    with open(path+'/star_gt_500.csv','r',encoding='utf-8') as f:
        flag = True
        for line in f:
            if flag:
                flag = False
                continue
            data = line.split(',')
            url = data[2]
            m_list.append(url)
    cnt = 0
    # max 0 2675
    for i in range(0,len(m_list)):
        print("No."+str(i))
        print(m_list[i])
        if m_list[i].startswith('https://github.com/liferay/liferay-portal'):
            continue
        data = m_list[i].split('/')
        m_path = '/home/fdse/data/prior_repository/'+data[-2]+'/'+data[-1]
        if not os.path.exists(m_path):
            continue
        flag = checkOneProj(m_path)
        if 'maven' in flag and 'gradle' in flag:
            print('proj-type: maven-gradle')
        else:
            if 'maven' in flag:
                print('proj-type: maven')
            elif 'gradle' in flag:
                print('proj-type: gradle')
            else:
                print('proj-type: no')
 
        #break


run()
