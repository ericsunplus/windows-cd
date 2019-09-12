import os
import argparse

databasefile = os.path.join(os.environ.get('userprofile'), 'dirstack.txt')

def pushdir(path):
    stackfile = open(databasefile, "a+")
    filelists = stackfile.read().splitlines()
    if path not in filelists:
        stackfile.seek(0, 2)
        stackfile.write(path + "\n")
    stackfile.close()

def cleanStackDataBase():
    stackfile = open(databasefile, "w+")
    stackfile.close()

def listDirStack():
    stackfile = open(databasefile, "r")
    filelists = stackfile.read().splitlines()
    stackfile.close()
    for num, name in enumerate(filelists, start=1):
        print "%-2d: %s" % (num, name)

def changdir(path):
    curDir = os.getcwd()
    targetDir = os.path.abspath(path)
    if os.path.isdir(targetDir) and targetDir != curDir:
        pushdir(curDir)
        print targetDir

def selectDir(number):
    stackfile = open(databasefile, "r")
    filelists = stackfile.read().splitlines()
    stackfile.close()
    changdir(filelists[number-1])

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="path to to switch to", nargs='?')
    parser.add_argument('-l', '--list', action='store_true', help='list directory stack')
    parser.add_argument('-s', '--select', type=int, help='select a dir in stack')
    parser.add_argument('-c', '--clean', action='store_true', help="clean directory stack database")
    args = parser.parse_args()

    if args.clean:
        cleanStackDataBase()
    elif args.list:
        listDirStack()
    elif args.select:
        selectDir(args.select)
    else:
        changdir(args.path)

if __name__ == '__main__':
    Main()
