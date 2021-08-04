#!/usr/bin/env python3
import os
# open file in read mode
os.chdir("/home/student/mycode/fact")
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
# close your file
dnsfile.close()

