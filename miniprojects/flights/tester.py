#!/usr/bin/env python3
import requests

API = 'http://api.aviationstack.com/v1/'
def credential():
    with open('flight.creds','r') as aviationFile:
        aviation = aviationFile.readline()
    return aviation.rstrip("\n")


def getFlights(creds,details):
    url =f'{API}{details}'
    params ={'access_key':creds}
    flight_data = requests.get(url,params).json()
    print(flight_data)
    return flight_data

def main():
    getFlights(credential(),'flights')


if __name__ == "__main__":
    main()
