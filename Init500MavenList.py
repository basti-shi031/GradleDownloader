import json
import os

if __name__ == '__main__':
    # initZipMap key:name value:path
    zip = {}
    # baseProject = '/home/fdse/sbw/mavenProject/'
    baseProject = '/home/fdse/sbw/mavenProject/'
    projectList = os.listdir(baseProject)
    for projectDir in projectList:
        projectZips = os.listdir(baseProject + projectDir)
        for projectZip in projectZips:
            if projectZip.endswith('.zip'):
                zip[projectZip] = baseProject + projectDir + '/' + projectZip
    print(zip)
    # # read all project whose star > 500
    f = open('java500_2.txt', 'r')
    allProject = f.read()
    f.close()
    allProjectJsonArray = json.loads(allProject)
    print(allProjectJsonArray)
    needZip = []
    zippedCount =0
    needZipCount = 0
    for projectJsonObject in allProjectJsonArray:
        proj = projectJsonObject['proj']
        name = proj.split('/')
        companyName = name[-2]
        projectName = name[-1]
        if companyName + '__fdse__' + projectName + '.zip' not in zip.keys():
            needZip.append(projectJsonObject)
            needZipCount+=1
        else:
            path = zip[companyName + '__fdse__' + projectName + '.zip']
            projectJsonObject['zippath'] = path
            zippedCount +=1
    print(allProjectJsonArray)
    f = open('maven500.txt', 'w')
    f.write(json.dumps(allProjectJsonArray))
    f.close()

    f = open('needZip.txt', 'w')
    f.write(json.dumps(needZip))
    f.close()
    print(needZipCount,zippedCount)
