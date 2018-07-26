import os

if __name__ == '__main__':
    baseProjectPath = 'H:/200-500/'
    # baseProjectPath = 'H:/test/'
    for index in range(1,19):
        projectsPath = baseProjectPath + str(index)
        projectList = os.listdir(projectsPath)
        for project in projectList:
            projectPath = projectsPath + '/' + project
            if os.path.isdir(projectPath):
                # if it is a dir , find its companyName in ./home/fdse/data/prior_repository/
                companyNamePath = projectPath + '/' + 'home/fdse/data/prior_repository'
                companyName = os.listdir(companyNamePath)[0]
                projectName = project
                os.rename(projectPath, projectsPath + '/' + companyName + '__fdse__' + projectName)
                os.rename(projectPath + '.zip', projectsPath + '/' + companyName + '__fdse__' + projectName + '.zip')
