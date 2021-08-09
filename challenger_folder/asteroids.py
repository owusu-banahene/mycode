#!/usr/bin/env python3
import requests
API = "https://api.nasa.gov/neo/rest/v1/feed"

def getData(start,end):
    params ={'start_date':start,
              'end_date':end,
              'api_key':getApi_Key()
              }
    data = requests.get(API,params).json()
    return data["near_earth_objects"]


def computeAsteroids(data):
    total = hazardous = 0
    biggest = fastest = closet =''
    big=fast=-1
    miss_size= 999999999999999999999

    if len(data) > 0:
        for key in data.keys():
            for asteroid in data[key]:
                total+=1
                if asteroid["is_potentially_hazardous_asteroid"]==True:
                    hazardous +=1
                if asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"] > big:
                    big = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
                    biggest = asteroid["name"]
                for close_data in asteroid["close_approach_data"]:
                    if float(close_data["relative_velocity"]["miles_per_hour"]) > fast:
                        fast = float(close_data["relative_velocity"]["miles_per_hour"])
                        fastest = asteroid["name"]
                    if float(close_data["miss_distance"]["kilometers"]) < miss_size:
                        miss_size = float(close_data["miss_distance"]["kilometers"])
                        closet= asteroid["name"]

    print(f"Number of asteroids present in this range is {total}")
    print(f"Number of hazardous asteriods present is {hazardous}")
    print(f"The biggest astroids in terms of kilometers is {biggest} with a value of {big}")
    print(f"The fastest astroids in terms of miles per hour is {fastest} with a value of {fast}")
    print(f"The closest astroids in terms of kilometers is {closet} with a value of {miss_size}")


def  getApi_Key():
    with open("nasa.creds","r") as nasafile:
        key = nasafile.readline()
    return key.rstrip("\n")


def main():
    print("Enter the start date inthe form YYYY-MM-DD: ")
    sDate=input(">").strip()
    print("Enter the end date in the form YYYY-MM-DD: ")
    eDate=input(">").strip()
    computeAsteroids(getData(sDate,eDate))


if __name__=="__main__":
    main()
