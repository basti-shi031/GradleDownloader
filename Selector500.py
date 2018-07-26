import json


# read projectType
def readAllProjectType(filename):
    f = open(filename, 'r')
    content = f.read()
    return json.loads(content)


# read project more than 500 star
def readAllProject500(filename):
    f = open(filename, 'r')
    content = f.read()
    return content.split('\n')[1:]


# getProjectType
# android : isAndroidProject
# maven : is Maven but not Android
# gradle : is Gradle but not Android
# maven_gradle : is Gradle and Maven but not Android
# error : not find in allProjectType from java3.txt
def getProjectType(companyName, projectName, allProjectType):
    for projectType in allProjectType:
        proj = projectType['proj']
        if companyName + '/' + projectName in proj:
            # find the project
            # then confirm its type
            android = projectType['android']
            gradle = projectType['gradle']
            maven = projectType['maven']
            if android:
                return 'android'
            if gradle and maven:
                return 'maven_gradle'
            if maven:
                return 'maven'
            if gradle:
                return 'gradle'
    return 'error'


if __name__ == '__main__':
    allProjectType = readAllProjectType('java3.txt')
    allProject = readAllProject500('starsmt500.csv')

    android = []
    maven = []
    gradle = []
    maven_gradle = []
    error = []
    for project in allProject:
        temp = project.split(',')
        url = temp[2]
        star = temp[3]
        companyName = url.split('/')[-2]
        projectName = url.split('/')[-1]
        type = getProjectType(companyName, projectName, allProjectType)
        fileName = companyName + '__fdse__' + projectName
        if type == 'android':
            android.append(fileName)
        elif type == 'maven':
            maven.append(fileName)
        elif type == 'gradle':
            gradle.append(fileName)
        elif type == 'maven_gradle':
            maven_gradle.append(fileName)
        elif type == 'error':
            error.append(fileName)
        else:
            print(fileName)

    print('==============')
    print(len(android))
    print(len(maven))
    print(len(gradle))
    print(len(maven_gradle))
    print(len(error))

    f = open('500/android500.txt','w')
    f.write(json.dumps(android))
    f.close()

    f = open('500/maven500.txt','w')
    f.write(json.dumps(maven))
    f.close()

    f = open('500/gradle500.txt','w')
    f.write(json.dumps(gradle))
    f.close()

    f = open('500/maven_gradle500.txt','w')
    f.write(json.dumps(maven_gradle))
    f.close()

    f = open('500/error500.txt','w')
    f.write(json.dumps(error))
    f.close()