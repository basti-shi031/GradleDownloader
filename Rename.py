import os

if __name__ == '__main__':
    baseProjectUrl = "/home/fdse/sbw/mavenProject/"
    max = 80
    for index in range(max):
        projectUrl = baseProjectUrl + str(index)
        projectList = os.listdir(projectUrl)
        for project in projectList:
            if '__fdse__' in project:
                print(index, project)
                projectName = project.split('__fdse__')[-1]
                print(projectUrl + '/' + project)
                print(projectUrl + '/' + projectName)
                os.rename(projectUrl + '/' + project, projectUrl + '/' + projectName)
