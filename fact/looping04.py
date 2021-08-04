#!/usr/bin/env python3
import os
os.chdir("/home/student/mycode/fact")
# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create list of lines
    # loop over lines
    for svr in dnsfile:
        svr = svr.rstrip("\n")
        if svr.endswith("org"):
            with open("org-domain.txt","a") as svrfile:
                svrfile.write(svr+"\n")
        elif svr.endswith("com"):
            with open("com-domain.txt","a") as svrfile:
                svrfile.write(svr+"\n")
# no need to close our file - closed automatically
