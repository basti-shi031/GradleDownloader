import json

if __name__ == '__main__':
    f = open('error500.txt', 'r')
    content = f.read()
    errorProjects = json.loads(content)
    f.close()

    f = open('500star.txt', 'r')
    content = f.read()
    f.close()

    content = content.split('\n')
    index = 0
    length = len(content)
    projectType = {}
    while index < length:
        line1 = content[index]
        line2 = content[index + 1]
        line3 = content[index + 2]
        index = index + 3
        companyName = line2.split('/')[-2]
        projectName = line2.split('/')[-1]
        print(line3)
        type = line3.split(': ')[1]
        projectType[companyName + '__fdse__' + projectName] = type

    error2 = []
    gradle = []
    maven = []
    maven_gradle = []
    for errorProject in errorProjects:
        if errorProject in projectType.keys():
            pass
            type = projectType[errorProject]
            if type == 'gradle':
                gradle.append(errorProject)
            elif type == 'maven':
                maven.append(errorProject)
            elif type == 'maven-gradle':
                maven_gradle.append(errorProject)
        else:
            error2.append(errorProject)

    print(len(error2))
    print(len(gradle))
    print(len(maven))
    print(len(maven_gradle))

    f = open('gradle500_2.txt', 'w')
    f.write(json.dumps(gradle))
    f.close()

    f = open('maven500_2.txt', 'w')
    f.write(json.dumps(maven))
    f.close()

    f = open('maven_gradle500_2.txt', 'w')
    f.write(json.dumps(maven_gradle))
    f.close()

    f = open('error500_2.txt', 'w')
    f.write(json.dumps(error2))
    f.close()