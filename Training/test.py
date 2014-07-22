#! /usr/bin/python2.7
import os
fileList =  os.popen('ls -lrt').readlines()
for eachLine in fileList:
    print eachLine 