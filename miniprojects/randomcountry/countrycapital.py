#!/usr/bin/env python3
#import choice from random
from random import choice
#import request to get data from external api
import requests

""" A program that allows a user to guess
the capital city of a randomly generated country"""
#a function to get the country-capital from REST API
def data():
     #the endpoint for the country api
    country_api = "https://restcountries.eu/rest/v2/"
    #fetch
    web_country = requests.get(country_api)
    countries_from_api = web_country.json()
    countries = {}
    for country in countries_from_api:
        #get the  country and capital from the json 
        countries[country["name"]] = country["capital"]
    return countries


def main():
    #get country data
    countries = data()
    play_game = True
    print("You have 3 chances to get it right\n")
    while play_game:
        #get a random country from the dictionary
        country_name = choice(list(countries.keys()))
        #print("You have 3 chances to get it right\n")
        print(f"What is the capital city of {country_name}")
        #get user_input
        user_input = input(">").strip().lower()
        #check user if user input are all characters
        if not user_input.isdigit():
            chance = 1
            while user_input != countries.get(country_name).lower():
                    print("You guessed wrong, try again")
                    user_input = input(">").strip().lower()
                    chance = chance + 1
                    if chance == 3:
                        print(f"You are out of guesses! The correct answer is {countries.get(country_name)}")
                        break

            if user_input == countries.get(country_name).lower():
                print(f"Correct!!!")
            print("Do you want to play again: (yes/no)")
            user_response = input(">").strip().lower()
            while user_response not in ["yes","y","no","n"]:
                user_response = input("Do you want to play again: (yes/no)").strip().lower()

            if user_response == "no" or user_response =="n":
                    print("Goodbye......")
                    play_game = False

        else:
             print(f"Invalid input {user_input}. Input must be all character[a-z][A-Z]")

if __name__ =="__main__":
    main()
