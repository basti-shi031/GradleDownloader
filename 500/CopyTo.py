import json
import shutil

if __name__ == '__main__':
    sourceFileName = 'maven_200_500_last.txt'
    destDir = 'F:/wangying/projects_last/maven200_500/'
    f = open(sourceFileName,'r')
    content = json.loads(f.read())
    f.close()

    for project in content:
        print(project,destDir)
        shutil.copy(project,destDir)