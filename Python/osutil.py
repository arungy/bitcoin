#!/usr/bin/env python

import sys
import os
import commands
#import os.path

def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print filename
        print os.path.join(dir, filename)
        print os.path.abspath(os.path.join(dir, filename))
    
    cmd = 'ls -l' + '/'
    print "Command to run:", cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print output
    
    try:
        f = open(filename, 'rU')
        text = f.read()
        f.close()
    except IOError:
        sys.stderr.write('problem reading:' + filename)
        
##url lib
def wget(url):
    ufile = urllib.urlopen(url)
    info = ufile.info()
    if info.gettype == 'text/html':
        print 'base url: ' + ufile.geturl()
        text = ufile.read()
        print text
        
def wget2(url):
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/html':
            print ufile.read()
    except IOError:
        print 'problem reading url:', url


def main():
    dir = dir(os.path) #'/cygdrive/c/DATA/work/learnpy/pyex/pytuto/'
    printdir(dir)


if '__name__' == '__main__':
    main()
    sys.exit(0)
