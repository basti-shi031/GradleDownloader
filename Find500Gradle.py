import json
import os


def readAllProject(filename):
    f = open(filename, 'r')
    return json.loads(f.read())


def getDownloadProject(path):
    downloadProjects = []
    projectDirs = os.listdir(path)
    for projectDir in projectDirs:
        projectList = os.listdir(path + projectDir)
        for project in projectList:
            if project.endswith('.zip'):
                downloadProjects.append(project)
    print(len(downloadProjects))
    return downloadProjects


# def getDownloadProject(path):
#     downloadProjects = []
#     projectDirs = os.listdir(path)
#     print(len(projectDirs))
#     return projectDirs

if __name__ == '__main__':

    downloadedProjects = getDownloadProject('d:/starProject/')
    print(downloadedProjects)
    fileArray = readAllProject('maven500.txt')

    cnt = 0
    cntdownload = 0
    cntnotdownload = 0
    cntnotmaven = 0
    cntandroid = 0
    for file in fileArray:
        isGradle = file['gradle']
        isMaven = file['maven']
        isAndroid = file['android']

        if isGradle and (not isAndroid):
            # find gradle but not android project
            cnt += 1
            proj = file['proj']
            companyName = proj.split('/')[-2]
            projectName = proj.split('/')[-1]
            fileName = companyName + '__fdse__' + projectName + '.zip'
            if fileName in downloadedProjects:
                file['download'] = True
                f = open('java500_2.txt', 'w')
                f.write(json.dumps(fileArray))
                f.close()
                cntdownload += 1
            else:
                print(fileName)
                file['download'] = False
                f = open('java500.txt', 'w')
                f.write(json.dumps(fileArray))
                f.close()
                cntnotdownload += 1
            if not isMaven:
                cntnotmaven += 1
    print(cnt, cntnotdownload, cntdownload, cntnotmaven)
