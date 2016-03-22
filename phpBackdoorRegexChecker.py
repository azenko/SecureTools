#!/usr/bin/python
import os, sys, getopt, hashlib, re

# Backdoor - PHP.M Regex
regex = "<\?php *\$[a-zA-Z0-9]* *= *\"[abcdeopst46_]{12}\" *; *\$[a-zA-Z0-9]* *\= *strtolower *\(.*\) *; *\$[a-zA-Z0-9]* *=.*strtoupper.*\(.*; *if *\(.*isset.*\${.*}.*eval.*\?\>"
regex = re.compile(regex)

def scan(foldertoScan):
    for dirname, dirnames, filenames in os.walk(foldertoScan):
        # print path to all filenames.
        for filename in filenames:
            fileuri = os.path.join(dirname, filename)
            with open(fileuri) as f:
                for line in f:
                    result = regex.search(line)
            if(result != None):
                print(fileuri)

def helpMe():
    print("Usage : <scriptname> <folderToScan>")

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        helpMe()
    elif(len(sys.argv) > 2):
        helpMe()
    else:
        scan(sys.argv[1])
