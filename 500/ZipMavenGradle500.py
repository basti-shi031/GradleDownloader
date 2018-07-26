import json
import os


def zipFiles(src, dest):
    sh = 'zip -r ' + dest + " " + src
    print(sh)
    os.popen(sh)


if __name__ == '__main__':
    f = open('maven_gradle500.txt', 'r')
    content = f.read()
    f.close()
    gradleProjects = json.loads(content)

    notDownloadGradle = []
    for project in gradleProjects:
        companyName = project.split('__fdse__')[0]
        projectName = project.split('__fdse__')[1]
        path = '/home/fdse/data/prior_repository/' + companyName + '/' + projectName
        if os.path.exists(path):
            zipFiles(path, 'maven_gradle500/' + project + '.zip')
        else:
            notDownloadGradle.append(project)
            f = open('notDownloadMavenGradle500.txt', 'w')
            f.write(json.dumps(notDownloadGradle))
            f.close()
