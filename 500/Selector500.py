import json
import os


def readProjects(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return json.loads(content)


def readSourceProjectDir(sourceProjectDir):
    sourceMaps = {}
    subDirs = os.listdir(sourceProjectDir)
    for subDir in subDirs:
        projects = os.listdir(sourceProjectDir + subDir)
        for project in projects:
            if os.path.isfile(sourceProjectDir + subDir + '/' + project):
                sourceMaps[project] = sourceProjectDir + subDir + '/' + project
    return sourceMaps


def readSourceProjectDir1(sourceProjectDir1, sourceMaps):
    projects = os.listdir(sourceProjectDir1)
    cnt1 = 0
    cnt2 = 0
    for project in projects:
        if os.path.isfile(sourceProjectDir1 + project):
            cnt1+=1
            sourceMaps[project] = sourceProjectDir1 + project

    path = sourceProjectDir1 + 'maven500/'
    projects = os.listdir(path)
    for project1 in projects:
        projectList = os.listdir(path+project1)
        for project2 in projectList:
            if os.path.isfile(path + project1+'/'+project2):
                cnt2 += 1
                sourceMaps[project2] = path + project1+'/'+project2
    return sourceMaps


if __name__ == '__main__':
    filename = 'maven500.txt'
    sourceProjectDir = 'D:/starProject/'
    sourceProjectDir2 = 'D:/maven500/'
    inFileName = 'maven500path.txt'
    notInFileName = 'maven500notinpath.txt'
    allProject = readProjects(filename)
    sourceMaps = readSourceProjectDir(sourceProjectDir)
    sourceMaps = readSourceProjectDir1(sourceProjectDir2, sourceMaps)
    print(sourceMaps)
    pathList = []
    notInList = []
    for project in allProject:
        if project + '.zip' in sourceMaps.keys():
            path = sourceMaps[project + '.zip']
            pathList.append(path)
        else:
            notInList.append(project)
    f = open(inFileName, 'w')
    f.write(json.dumps(pathList))
    f.close()

    f = open(notInFileName, 'w')
    f.write(json.dumps(notInList))
    f.close()
