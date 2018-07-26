import json
import os
import shutil

if __name__ == '__main__':
    f = open('maven500.txt', 'r')
    mavenProjectArray = json.loads(f.read())
    f.close()
    for mavenProjectObject in mavenProjectArray:
        if 'zippath' not in mavenProjectObject.keys():
            mavenProjectObject['move'] = False
            mavenProjectObject['problem'] = True
            fread = open('maven500.txt', 'w')
            fread.write(json.dumps(mavenProjectArray))
            fread.close()
            continue
            print('fail')
            continue
        zipPath = mavenProjectObject['zippath']
        destPath = 'maven500/'
        dest = destPath + zipPath.split('/')[-1]
        if not os.path.exists(zipPath):
            print('fail')
            print(zipPath)
            mavenProjectObject['move'] = False
            mavenProjectObject['problem'] = True
            fread = open('maven500.txt', 'w')
            fread.write(json.dumps(mavenProjectArray))
            fread.close()
            continue
        if not os.path.exists(destPath):
            os.makedirs(destPath)
        print('success')
        shutil.copy(zipPath, destPath + zipPath.split('/')[-1])
        mavenProjectObject['move'] = True
        fread = open('maven500.txt', 'w')
        fread.write(json.dumps(mavenProjectArray))
        fread.close()
