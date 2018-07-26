import json


def download():
    pass


if __name__ == '__main__':
    # 读取列表
    f = open('maven500.txt', 'r')
    content = f.read()
    f.close()
    mavenProjectList = json.loads(content)

    # download each maven project
    for mavenProject in mavenProjectList:
        if 'download' not in mavenProject.keys():
            download(mavenProject['zippath'],'d:/maven500/')
            mavenProject['download'] = True
            fread = open('maven500.txt', 'w')
            fread.write(json.dumps(mavenProjectList))
            f.close()
