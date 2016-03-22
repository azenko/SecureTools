#!/usr/bin/python#!/usr/bin/python
import os, sys, getopt, hashlib

def scan(foldertoScan):
    for dirname, dirnames, filenames in os.walk(foldertoScan):
        # print path to all filenames.
        for filename in filenames:
            fileuri = os.path.join(dirname, filename)
            filemd5 = hashlib.md5(open(fileuri,'rb').read()).hexdigest()
            print(filemd5)

def helpMe():
    print("Usage : <scriptname> <folderToScan>")

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        helpMe()
    elif(len(sys.argv) > 2):
        helpMe()
    else:
        scan(sys.argv[1])
