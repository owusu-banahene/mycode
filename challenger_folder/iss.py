#!/usr/bin/env python3
import requests
import time
import reverse_geocoder as rg

def getISS():
    API="http://api.open-notify.org/iss-now.json"
    data = requests.get(API).json()
    coord = (data["iss_position"]["latitude"],data["iss_position"]["longitude"])
    print('CURRENT LOCATION OF THE ISS:')
    print(f'Timestamp: {convertToHumans(data["timestamp"])}')
    print(f'Lon: {data["iss_position"]["longitude"]}')
    print(f'Lat: {data["iss_position"]["latitude"]}')
    print(f'City: {getCity(coord)}')


def convertToHumans(etime):
    return time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(etime))

def getCity(coordinates):
    city = rg.search(coordinates)
    return city[0]["name"]
    

def main():
    getISS()


if __name__=="__main__":
    main()
