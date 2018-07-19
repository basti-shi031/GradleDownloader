import json
import os
import sys
import zipfile


def zip_file(startdir, file_news):
    print(startdir)
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            print('==', dirpath, '===', dirnames, '===', filename)
            if os.path.exists(dirpath + '/' + filename):
                z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


def isMaven(company, project):
    name = company + '/' + project
    for pro in data:
        if name in pro.get('proj'):
            return True
    return False


if __name__ == '__main__':
    homePath = '/home/fdse/sbw/mavenProject/'
    index = sys.argv[1]
    index = int(index)
    max = 20
    count = 0
    f1 = open('1.json', 'r')
    content = f1.read()
    data = json.loads(content)
    f2 = open('downloadedMaven.txt', 'r+')
    projects = f2.read()
    print(projects)
    basePath = '/home/fdse/data/prior_repository/'
    companyList = os.listdir(basePath)
    for company in companyList:
        companyPath = basePath + company + "/"
        projectList = os.listdir(companyPath)
        for project in projectList:
            print(project)
            print(project in projects)
            if project in projects:
                print('download')
                continue
            elif isMaven(company, project):
                print('is Maven')
                newPath = homePath + str(index)
                print(newPath)
                if not os.path.exists(newPath):
                    os.makedirs(newPath)
                print(newPath + '/' + project + '.zip')
                zip_file(companyPath + project, newPath + "/" + project + '.zip')
                projects = projects + ",'" + project + "'"
                f2.write(",'" + project + "'")
                count += 1
                if count >= max:
                    index += 1
                    count = 0
            else:
                print('is not Maven')
