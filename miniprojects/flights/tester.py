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


def getflights(creds,details):
    url =f'{API}{details}'
    params ={'access_key':creds
            }
    flight_data = requests.get(url,params).json()
    #print(flight_data["data"])
    return flight_data["data"]


def getstatusflights(flights):
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
    getdetails(cancelled,'Cancellation')
    getdetails(active,'Active')
    getdetails(scheduled,'Scheduled Flight')
    getdetails(landed,'Landed')
    getdetails(incident,'Flights with incident')
    getdetails(diverted,'Flights that were diverted ')



def getairlinescount(flight_data):
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

def statusplots(statusdata,filename):
    status_df = pd.json_normalize(statusdata)
    print(status.head(10))


def getdetails(statusdata,status):
    if len(statusdata) > 0:
        print("\n")
        print(f"{status} summary")
        print("================================")
        status_df = pd.DataFrame.from_dict(getairlinescount(statusdata),orient='index')
        status_df.reset_index(level=0,inplace=True)
        status_df.columns=['airline_name','occurrence']
        #sort by occurrence in descending
        status_df.sort_values(by='occurrence',inplace=True,ascending=False)
        #print top 5
        print(status_df.head(5).to_string(index=False))
        #plt.title(status)
        status_df.plot.barh(x='airline_name',y='occurrence')
        plt.title(status)
        plt.show()
        plt.savefig(f'/home/student/static/{status}.png')
        #print(f"{status} Summary")
        #print("============================")
        #for cancel in statusData:
        #    pprint(f"{cancel['airline']['name']} from {cancel['departure']['airport']} to {cancel['arrival']['airport']}")
        #print("\n")



def visualizedata(vflights):
    visualize = pd.json_normalize(vflights)
    visualize = visualize[['flight_date','flight_status','aircraft','departure.airport','arrival.airport','airline.name']]
    #pprint(visualize.head(10))
    return visualize


def main():
    current_data=getflights(credential(),'flights')
    getstatusflights(current_data)
    print()
    #print("Types of airline and their count:")
    #print(getairlinescount(current_data))
    #visualize data
    subflights = visualizedata(current_data)
    #limit it to cancelled flights
    print("Cancellation flights details")
    print("================================================================================================================================================================")
    subflights = subflights[subflights['flight_status'] =='cancelled']
    print(subflights.to_string(index=False))


if __name__ == "__main__":
    main()
