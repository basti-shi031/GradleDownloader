import json

if __name__ == '__main__':
    f = open('maven_gradle500.txt', 'r')
    content = f.read()
    jsons = json.loads(content)

    print(len(jsons))
    print(len(set(jsons)))