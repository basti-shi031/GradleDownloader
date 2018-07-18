# 生成已下载项目列表
import os

if __name__ == '__main__':
    fileList = []
    path = "F:/wangying/mavenProject/mavenProject/"
    for index in range(19):
        projectsFile = path + str(index)
        projects = os.listdir(projectsFile)
        for project in projects:
            fileList.append(project)
    print(fileList)