#!/usr/bin/env python3
import requests
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

API = 'https://api.aviationstack.com/v1/'


def credential():
    with open('flight.creds','r') as aviationFile:
        aviation = aviationFile.readline()
    return aviation.rstrip("\n")


def getFlights(creds,details):
    url =f'{API}{details}'
    params ={'access_key':creds
            }
    flight_data = requests.get(url,params).json()
    #print(flight_data["data"])
    return flight_data["data"]


def getStatusFlights(flights):
    active=[]
    scheduled=[]
    landed=[]
    cancelled=[]
    incident=[]
    diverted=[]
    #print(f"In get live data {len(flights)}")
    for flight in flights:
        if flight["flight_status"] == "active":
            active.append(flight)
        elif flight["flight_status"] == "scheduled":
            scheduled.append(flight)
        elif flight["flight_status"] == "landed":
            landed.append(flight)
        elif flight["flight_status"] == "cancelled":
            cancelled.append(flight)
        elif flight["flight_status"] == "incident":
            incident.append(flight)
        else:
            diverted.append(flight)
        
    print(f"Out of 100 sample flights: active={len(active)},scheduled={len(scheduled)},landed={len(landed)},cancelled={len(cancelled)},incident={len(incident)} and diverted={len(diverted)}")
    #print("Cancelled Flights Summary")
    #pprint(getAirlinesCount(cancelled))
    #getDetails(cancelled,'Cancellation')
    #getDetails(active,'Active')
    #getDetails(scheduled,'Scheduled Flight')
    #getDetails(landed,'Landed')
    #getDetails(incident,'Flights with incident')
    #getDetails(diverted,'Flights that were diverted ')



def getAirlinesCount(flight_data):
    name_of_airline ={}
    for flight in flight_data:
        if flight["airline"]["name"] in name_of_airline.keys():
            current_value = name_of_airline.get(flight['airline']["name"]) 
            current_value +=1
            name_of_airline[flight['airline']['name']] = current_value
        else:
            name_of_airline[flight['airline']['name']] = 1

    #print(name_of_airline)
    return name_of_airline


def getDetails(statusData,status):
    if len(statusData) > 0:
        print(f"{status} Summary")
        print("============================")
        for cancel in statusData:
            pprint(f"{cancel['airline']['name']} from {cancel['departure']['airport']} to {cancel['arrival']['airport']}")
        print("\n")



def visualizeData(vflights):
    visualize = pd.json_normalize(vflights)
    visualize = visualize[['flight_date','flight_status','aircraft','departure.airport','arrival.airport','airline.name']]
    pprint(visualize.head(10))
    return visualize


def main():
    current_data=getFlights(credential(),'flights')
    getStatusFlights(current_data)
    print()
    print("Types of airline and their count:")
    print(getAirlinesCount(current_data))
    #visualize data
    subflights = visualizeData(current_data)
    #flights with more than 4 cancellation occurrance
    subflights['airline.name'].value_counts().loc[lambda x:x>4].plot(kind='barh')
    plt.show()
    plt.savefig('/home/student/static/more_than_four_cancel_flight.png')
     #flights less than 2  cancellation occurrance
    subflights['airline.name'].value_counts().loc[lambda x:x<2].plot(kind='barh')
    plt.show()
    plt.savefig('/home/student/static/less_than_two_cancel_flight.png')
     #flights between 2 andn 4 cancellation occurrance
    #subflights['airline.name'].value_counts().loc[lambda x:x >=2 & x <=4].plot(kind='barh')
    #plt.show()
    #plt.savefig('/home/student/static/between_two_and_four_cancel_flight.png')


if __name__ == "__main__":
    main()
