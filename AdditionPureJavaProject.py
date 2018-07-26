import json
import os

import queue

passfile = ['.git', 'gradle', '.idea', 'res']


# bfs
def isProject(path, fileName):
    q = queue.Queue()
    q.put(path)
    while not q.empty():
        f = q.get()
        if os.path.isdir(f):
            files = os.listdir(f)
            for file in files:
                if file in passfile:
                    continue
                if os.path.isfile(f + '/' + file):
                    if fileName == file.lower():
                        return True
                else:
                    q.put(f + '/' + file)
        elif os.path.isfile(f):
            if fileName in f.lower():
                return True
    return False


def isAndroidProject(path):
    return isProject(path, 'androidmanifest.xml')


def isMavenProject(path):
    return isProject(path, 'pom.xml')


# if __name__ == '__main__':
#     f1 = open('1.json', 'r')
#     content = f1.read()
#     data = json.loads(content)
#     print(len(data))
#     f1.close()
#     projectList = []
#     fchecked = open('hasCheckedIsJava3.txt', 'r')
#     isJavaStr = fchecked.read()
#     hasCheckedIsJava = json.loads(isJavaStr)
#     maven = []
#     for item in data:
#         proj = item['proj']
#         print(proj)
#         if proj in hasCheckedIsJava.keys():
#             print("checked")
#             continue
#         isMaven = item['maven']
#         isGradle = item['gradle']
#         print(isGradle, isMaven)
#         if not (isGradle or isMaven):
#             # isRealMaven = isMavenProject(proj)
#             # print(isRealMaven)
#             if isRealMaven:
#                 isAndroid = isAndroidProject(proj)
#                 maven.append(proj)
#                 print(isAndroid)
#                 if not isAndroid:
#                     projectList.append(proj)
#                     print(len(projectList))
#                     java2 = open('java3.txt', 'w')
#                     java2.write(json.dumps(projectList))
#                     java2.close()
#         hasCheckedIsJava[proj] = True
#         fchecked = open('hasCheckedIsJava3.txt', 'w')
#         fchecked.write(json.dumps(hasCheckedIsJava))
#         fchecked.close()
#     print(maven)
#     print(len(projectList))
#     print(projectList)
if __name__ == '__main__':
    projects = json.loads(open('500/error500.txt', 'r').read())
    for project in projects:
        companyName = project.split('__fdse__')[0]
        projectName = project.split('__fdse__')[1]
        path = '/home/fdse/data/prior_repository/' + companyName + '/' + projectName
        