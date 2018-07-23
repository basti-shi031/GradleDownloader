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


def zip_batch(fileList):
    limitSize = len(newFileList)
    fileIndex = 15
    currentCount = 0
    maxFileCount = 20
    for i in range(4, len(newFileList)):
        filePath = newFileList[i]
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

def zip_bash(fileList):
    limitSize = len(newFileList)
    fileIndex = 15
    currentCount = 0
    maxFileCount = 20
    for i in range(0, len(newFileList)):
        filePath = newFileList[i]
        dirPath = 'mavenProject/' + str(fileIndex)
        print(str(i) + "====" + dirPath + "====" + filePath)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        sh = 'zip -r ./'+dirPath+"/"+filePath.split('/')[-1]+'.zip /home/fdse/'+filePath.replace('..','.')[2:]
        content = os.popen(sh)
        print(sh)
        a = content.read()
        currentCount += 1
        if currentCount == maxFileCount:
            fileIndex += 1
            currentCount = 0
            print("============" + str(fileIndex) + "============")


if __name__ == '__main__':
    fileList = []
    with open('pro.txt', 'r') as f:
        for line in f:
            if line.startswith('..'):
                fileList.append(line.strip('\n'))
    newFileList = []
    with open('pro2.txt', 'r') as f:
        for line in f:
            if line.startswith('..'):
                line = line.strip('\n')
                if line not in fileList:
                    newFileList.append(line)
    print(len(newFileList))
    zip_bash(newFileList)
    
