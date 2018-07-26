import json
import os


def write(fileName, content):
    f = open(fileName, 'w')
    f.write(json.dumps(content))
    f.close()


def initFileMaps():
    baseProjectPath = 'f:/wangying/projects/'
    dirs = os.listdir(baseProjectPath)
    for dir in dirs:
        path = baseProjectPath + dir + '/'
        projectNames = os.listdir(path)
        for project in projectNames:
            fileMaps[project] = path + project
    return fileMaps


def initFileMaps2(fileName,fileMaps):
    dirs = os.listdir(fileName)
    for project in dirs:
        path = fileName + project
        fileMaps[project] = path
    return fileMaps


if __name__ == '__main__':
    fileMaps = {}
    fileMaps = initFileMaps2('I:/maven_200_500_zip/', fileMaps)
    print(len(fileMaps))

    fileMaps = initFileMaps2('I:/gradle_200_500_zip/',fileMaps)

    print(len(fileMaps))
    f = open('star200-500.txt', 'r')
    content = f.read()
    f.close()
    projects = content.split('\n')

    length = len(projects)
    index = 0

    gradles = []
    mavens = []
    gradle_mavens = []

    gradle_not_in = []
    maven_not_in = []
    gradle_maven_not_in = []

    while index < length:
        line1 = projects[index]
        line2 = projects[index + 1]
        line3 = projects[index + 2]
        if 'proj-type' not in line3:
            index += 2
        else:
            index += 3
            type = line3.split(': ')[1].strip()
            companyName = line2.split('/')[-2]
            projectName = line2.split('/')[-1]
            if type == 'android':
                continue
            fileName = companyName + '__fdse__' + projectName + '.zip'
            if fileName not in fileMaps.keys():
                if type == 'gradle':
                    gradle_not_in.append(fileName)
                elif type == 'maven':
                    maven_not_in.append(fileName)
                elif type == 'maven-gradle':
                    gradle_maven_not_in.append(fileName)
            else:
                path = fileMaps[fileName]
                if type == 'gradle':
                    gradles.append(path)
                elif type == 'maven':
                    mavens.append(path)
                elif type == 'maven-gradle':
                    gradle_mavens.append(path)

    print(len(gradles))
    print(len(gradle_not_in))
    print(len(mavens))
    print(len(maven_not_in))
    print(len(gradle_mavens))
    print(len(gradle_maven_not_in))
    write('gradle_200_500_last.txt', gradles)
    write('gradle_200_500_not_in_last.txt', gradle_not_in)
    write('maven_200_500_last.txt', mavens)
    write('maven_200_500_not_in_last.txt', maven_not_in)
    write('gradle_maven_200_500_last.txt', gradle_mavens)
    write('gradle_maven_200_500_not_in_last.txt', gradle_maven_not_in)
