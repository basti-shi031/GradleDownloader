import os
import sys
import zipfile


def zip_file(startdir, file_news):
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


def formatFileName(name):
    tempName = name.split('.zip')[0].split('__fdse__')
    return tempName[0] + "-" + tempName[1]


def initZipFile(index, zipFiles, dest):
    for i in range(1, index + 1):
        realDest = dest + str(i) + "//"
        ls = os.listdir(realDest)
        zipFiles.extend(map(formatFileName, ls))


if __name__ == '__main__':
    zipFiles = []
    root = sys.argv[1]
    dest = sys.argv[2]
    index = sys.argv[3]
    index = int(index)
    count = 0
    initZipFile(index, zipFiles, dest)
    print(zipFiles)
    index += 1
    realDest = dest + str(index) + "//"
    if not os.path.exists(realDest):
        os.makedirs(realDest)
    ls = os.listdir(root)
    print('============'+str(index)+'===============')
    for file in ls:
        company_path = root + '//' + file
        projects = os.listdir(company_path)
        for project in projects:
            project_path = company_path + '//' + project
            print("ttt "+file+"-"+project)
            print(file+"-"+project not in zipFiles)
            if 'build.gradle' in os.listdir(project_path) and file+"-"+project not in zipFiles:
                print(project)
                zip_file(project_path, realDest + file + '__fdse__' + project + '.zip')
                count += 1
                if count == 20:
                    index += 1
                    count = 0
                    print('============' + str(index) + '===============')
                    realDest = dest + str(index) + "//"
                    if not os.path.exists(realDest):
                        os.makedirs(realDest)
