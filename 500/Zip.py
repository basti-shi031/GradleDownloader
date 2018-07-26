import os


def zipFiles(src, dest):
    sh = 'zip -r ' + dest + " " + src
    print(sh)
    os.popen(sh)
