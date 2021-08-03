 #!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
    Alta3 Research | rzfeeser@alta3.com"""

import shutil  
import os      
def main():
     """called at runtime"""
     os.chdir('/home/student/mycode/')  
     shutil.move('raynor.obj', 'ceph_storage/') 

     # program will pause while we accept input
     xname = input('What is the new name for kerrigan.obj? ') 
     shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ =="__main__":
        main()


