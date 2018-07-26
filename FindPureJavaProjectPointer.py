import json
import os

passfile = ['.git', 'gradle', '.idea', 'res']
count = 0


def isAndroidProject(path):
    files = os.listdir(path)
    for file in files:
        if file in passfile:
            continue
        if os.path.isdir(path + "/" + file):
            isAndroid = isAndroidProject(path + "/" + file)
            if isAndroid:
                return True
        elif os.path.isfile(path + "/" + file):
            if 'androidmanifest.xml' == file.lower():
                return True
    return False


if __name__ == '__main__':
    f1 = open('1.json', 'r')
    content = f1.read()
    data = json.loads(content)
    print(len(data))
    f1.close()
    projectList = []
    fchecked = open('hasCheckedIsJava.txt', 'r')
    isJavaStr = fchecked.read()
    hasCheckedIsJava = json.loads(isJavaStr)
    fchecked.close()
    for item in data:
        proj = item['proj']
        print(item['proj'])
        if proj in hasCheckedIsJava.keys():
            print("checked")
            continue
        isMaven = item['maven']
        isGradle = item['gradle']
        # isAndroid = isAndroidProject(item['proj'])
        print('isMaven:', isMaven, 'isGradle.', isGradle)
        if isMaven or isGradle:
            isAndroid = isAndroidProject(item['proj'])
            print('isAndroid', isAndroid)
            if not isAndroid:
                project = {}
                project['proj'] = item['proj']
                project['maven'] = True
                project['gradle'] = True
                project['android'] = False
                projectList.append(project)
                java2 = open('java2.txt', 'w')
                java2.write(json.dumps(projectList))
        print(len(projectList))
        hasCheckedIsJava[proj] = True
        fchecked = open('hasCheckedIsJava.txt', 'w')
        fchecked.write(json.dumps(hasCheckedIsJava))
        fchecked.close()
# f2 = open('java2.txt', 'r+')
# f2.read()
# f2.write(json.dumps(projectList))
