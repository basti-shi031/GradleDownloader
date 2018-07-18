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
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


if __name__ == '__main__':
    index = sys.argv[1]
    index = int(index)
    f = open('pro.txt', 'r')
    content = f.read()
    numFileList = content.split("\n")
    print(len(numFileList))
    limitSize = len(numFileList)
    fileIndex = 14
    currentCount = 0
    maxFileCount = 20
    for i in range(0, len(numFileList) - 1, 2):
        num = numFileList[i]
        if int(num) >= index:
            filePath = numFileList[i + 1]
            dirPath = 'mavenProject//' + str(fileIndex)
            print(str(i) + "====" + dirPath + "====" + filePath)
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
            zip_file('//home//fdse' + filePath.replace('..', '').replace('/', '//'),
                     dirPath + "//" + filePath.split('/')[-1]+'.zip')
            currentCount += 1
            if currentCount == maxFileCount:
                fileIndex += 1
                currentCount = 0
                print("============" + str(fileIndex) + "============")
# zipFiles = []
# root = sys.argv[1]
# dest = sys.argv[2]
# index = sys.argv[3]
# print('============' + str(index) + '===============')
# for file in ls:
#     company_path = root + '//' + file
#     projects = os.listdir(company_path)
#     for project in projects:
#         project_path = company_path + '//' + project
#         print("ttt " + file + "-" + project)
#         print(file + "-" + project not in zipFiles)
#         if 'build.gradle' in os.listdir(project_path) and file + "-" + project not in zipFiles:
#             print(project)
#             zip_file(project_path, realDest + file + '__fdse__' + project + '.zip')
#             count += 1
#             if count == 20:
#                 index += 1
#                 count = 0
#                 print('============' + str(index) + '===============')
#                 realDest = dest + str(index) + "//"
#                 if not os.path.exists(realDest):
#                     os.makedirs(realDest)
