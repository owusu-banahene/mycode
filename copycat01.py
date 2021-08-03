#!/usr/bin/env python3
import shutil
import os

def main():
    """code to move files around"""
    os.chdir("/home/student/mycode")
    shutil.copy("5g_research/sdn_network.txt","5g_research/sdn_network.txt.copy")
    shutil.copytree("5g_research/","5g_research_backup/")

if __name__ == "__main__":
    main()
