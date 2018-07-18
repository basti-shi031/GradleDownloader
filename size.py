import os
import sys

if __name__ == '__main__':
    root = sys.argv[1]
    ls = os.listdir(root)
    size = 0;
    for file in ls:
        company_path = root + '//' + file
        projects = os.listdir(company_path)
        for project in projects:
            project_path = company_path + '//' + project
            if 'build.gradle' in os.listdir(project_path):
                print(project)
                size = size + 1;
    print(size)
