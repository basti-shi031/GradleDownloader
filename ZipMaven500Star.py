import json
import os
import sys


def zip_file2(dir, file_news):
    sh = 'zip -r ' + file_news + " " + dir
    print(sh)
    print(os.popen(sh))


if __name__ == '__main__':
    # read all projects have zipped
    baseProject = '/home/fdse/sbw/mavenProject/'
    zippedFiles = []
    projectDirs = os.listdir(baseProject)
    for projectDir in projectDirs:
        projectList = os.listdir(baseProject + projectDir)
        zippedFiles.extend(projectList)
    print(len(zippedFiles))
    # read all project whose star > 500
    f = open('java500.txt', 'r')
    allProject = f.read()
    allProjectJsonArray = json.loads(allProject)
    max = 20
    index = sys.argv[1]
    index = int(index)
    count = 0

    cnt = 0
    for project in allProjectJsonArray:
        # /home/fdse/data/prior_repository/Netflix/SimianArmy

        cnt += 1
        print(cnt)
        print(project['proj'])
        isMaven = project['maven']
        print(isMaven)
        if isMaven:
            temp = project['proj'].split('/')
            companyName = temp[-2]
            projectName = temp[-1]
            if projectName + '.zip' in zippedFiles or companyName + '__fdse__' + projectName + '.zip' in zippedFiles:
                print('in')
                continue
            if not os.path.exists(baseProject + str(index) + '/'):
                os.makedirs(baseProject + str(index) + '/')
            zip_file2(project['proj'], baseProject + str(index) + '/' + projectName + '.zip')
            count += 1
            if count >= max:
                count = 0
                index += 1
