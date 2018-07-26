import os
import shutil


def convertName(path):
    projectName = path.split('/')[-1]
    companyName = os.listdir(path + '/' + 'home/fdse/data/prior_repository/')[0]
    os.rename(path, path.split(projectName)[0] + companyName + '__fdse__' + projectName)
    os.rename(path + 'zip', path.split(projectName)[0] + companyName + '__fdse__' + projectName + '.zip')


def rename(sour, dest):
    os.rename(sour, dest)


def readOutContent(fileName):
    f = open(fileName, 'r')
    content = f.read()
    f.close()
    return content.split('\n')


def getLocalPathByFileName(fileName):
    pass


def getLocalPathByContent(line1, line2, line3, line4):
    # No.0
    # Id.4
    # https://github.com/SpoutDev/Spout
    # proj-type: No
    isAndroidStr = line4.split(':')[1].strip()
    if isAndroidStr == 'No':
        companyName = line3.split('/')[-2]
        projectName = line4.split('/')[-1]
        fileName = companyName + '__fdse__' + projectName
        return getLocalPathByFileName(fileName)
    else:
        return ''


def copyTo(source, dest):
    shutil.copy(source, copy)


if __name__ == '__main__':
    # find all project in map
    baseUrl = 'H:/200-500/'
    dirs = os.listdir(baseUrl)
    fileMap = {}
    for dir in dirs:
        projectlist = os.listdir(baseUrl + dir)
        for project in projectlist:
            if os.path.isdir(baseUrl + dir + '/' + project):
                companyName = project.split('__fdse__')[0]
                projectName = project.split('__fdse__')[1]
                fileMap[project] = baseUrl + dir + '/' + project
    #     ==============================================================
    # content = readOutContent('C:/Users/Basti031/Desktop/gradleandmaven/7-22-maven.out')
    content = readOutContent('C:/Users/Basti031/Desktop/gradleandmaven/7-22-gradle.out')
    contentLength = len(content)
    contentLength = contentLength - contentLength % 4
    index = 0
    while index < contentLength:
        line1 = content[index]
        line2 = content[index + 1]
        line3 = content[index + 2]
        line4 = content[index + 3]
        index += 4
        isAndroid = line4.split(':')[1].strip()
        if isAndroid == 'No':
            # not android
            companyName = line3.split('/')[-2]
            projectName = line3.split('/')[-1]
            fileName = companyName + '__fdse__' + projectName
            if fileName not in fileMap.keys():
                print(fileName + 'not in')
            else:
                filePath = fileMap[fileName]
                print(filePath)
                shutil.copy(filePath + '.zip', 'H:/gradle_200_500_zip/')
