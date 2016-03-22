#!/usr/bin/python
import os, sys, getopt, hashlib

def scan(foldertoScan, hashListFile, hashType, showMd5):
    fileHash = {}

    #Load hashList
    hashList = [line.rstrip('\n') for line in open(hashListFile)]

    #Load fileHashList
    if(hashType == "md5"):
        for dirname, dirnames, filenames in os.walk(foldertoScan):
            # print path to all filenames.
            for filename in filenames:
                fileuri = os.path.join(dirname, filename)
                filemd5 = hashlib.md5(open(fileuri,'rb').read()).hexdigest()
                fileHash[fileuri] = filemd5

        #Compare Hash
        for file in fileHash.keys():
            if(fileHash[file] not in hashList):
                if(showMd5):
                    print(file + " : " + fileHash[file])
                else:
                    print(file)
    else:
        helpMe()
        quit()

def helpMe():
    print("Usage : <scriptname>  <folderToScan> <hashList> <hashType> [showMd5]")
    print("Supported HashType : md5")

if __name__ == '__main__':
    # Fonctionnement : <scriptname> folderToScan hashList.txt <hashType>
    # Supported HashType : md5, sha1
    if(len(sys.argv) < 4):
        helpMe()
    elif(len(sys.argv) == 4):
        scan(sys.argv[1], sys.argv[2], sys.argv[3], 0)
    elif(len(sys.argv) > 5):
        helpMe()
    else:
        scan(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
