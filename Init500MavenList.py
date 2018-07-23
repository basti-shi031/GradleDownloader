import json
import os

if __name__ == '__main__':
    # initZipMap key:name value:path
    zip = {}
    baseProject = '/home/fdse/sbw/mavenProject/'
    projectList = os.listdir(baseProject)
    for projectDir in projectList:
        projectZips = os.listdir(baseProject + projectDir)
        for projectZip in projectZips:
            zip[projectZip] = baseProject + projectDir + '/' + projectZip
    # # read all project whose star > 500
    f = open('java500.txt', 'r')
    allProject = f.read()
    f.close()
    allProjectJsonArray = json.loads(allProject)
    print(allProjectJsonArray)
    for projectJsonObject in allProjectJsonArray:
        proj = projectJsonObject['proj']
        name = proj.split('/')
        companyName = name[-2]
        projectName = name[-1]
        path = zip[projectName + '.zip']
        projectJsonObject['zippath'] = path
    print(allProjectJsonArray)
    f = open('maven500.txt', 'w')
    f.write(json.dumps(allProjectJsonArray))
    f.close()
