import os

if __name__ == '__main__':
    fileList = []
    path = "/home/fdse/sbw/mavenProject/"
    for index in range(33):
        projectsFile = path + str(index)
        projects = os.listdir(projectsFile)
        for project in projects:
            fileList.append(project)
    print(fileList)
    f = open('zippedProject.txt','r+')
    f.read()
    for file in fileList:
        f.write(file.split('.')[0]+" ")
    f.close()
