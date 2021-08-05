#!/usr/bin/env python3
import json
import os
def commandpush(devicemd):

    for ip in devicemd.keys():
        print(f"Handsking. .. ... connecting with {ip}")
        for mycmds in devicemd.get(ip):
            print(f"Atteming to send command --> {mycmds}")

    return None

def devicereboot(ips):
    for ip in ips:
        print(f"Connecting to ..{ip}")
        print("REBOOTING NOW!")




def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    os.chdir("/home/student/mycode/netfunct01")
    with open("commands.json","r") as commandfile:
        devicecmd = json.load(commandfile)
    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    ## passing the ips to devicereboot function
    devicereboot(devicecmd.keys())


main()
