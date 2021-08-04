#!/usr/bin/env python3
#farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
#         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
 #        {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

list_animal=["sheep","cows","pigs","chickens","llamas","cats"]

def function1():
    print("Returning all animals from NE Farm")
    for farm in farms:
        if farm.get("name") == "NE Farm":
            for eachanimal in farm.get("agriculture"):
                print(eachanimal)


def function2():
    #get user_input
    print("Returning both plants and animals for a given farm...")
    print("Choose a farm (NE Farm, W Farm, SE Farm,or E Farm)")
    user_input = input(">").strip().lower()
    for farm in farms:
        if farm.get("name").lower()==user_input:
            for plant_animal in farm.get("agriculture"):
                print(plant_animal)

def function3():
    #user input
    print("Returning only animals for a given farm")
    print("Choose a farm (NE Farm, W Farm, E Farm or SE Farm")
    user_input=input(">").strip().lower()
    for farm in farms:
        if farm.get("name").lower() == user_input:
            for animal in farm.get("agriculture"):
                if animal in list_animal:
                    print(animal)

if __name__ =="__main__":
    function1()
    function2()
    function3()
