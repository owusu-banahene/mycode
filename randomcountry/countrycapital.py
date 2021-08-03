#!/usr/bin/env python3
#import choice from random
from random import choice
""" A program that allows a user to guess
the capital city of a randomly generated country"""
#declare a dictionary for the countries and their capital
countries={
   "Afghanistan": "Kabul", "Angola": "Luanda", "Austria": "Vienna", "Belgium": "Brussels", "Burkina Faso": "Ouagadougou",
   "Canada": "Ottawa", "Chile": "Santiago","China": "Beijing","Cuba": "Havana", "Czech Republic": "Prague",
   "Denmark": "Copenhagen","Djibouti": "Djibouti","Dominican Republic": "Santo Domingo","Egypt": "Cairo",
   "Ethiopia": "Addis Ababa","El Salvador": "San Salvador","France": "Paris","Finland": "Helsinki","Fiji": "Suva",
   "Gabon": "Libreville","Germany": "Berlin","Greece": "Athens","Ghana": "Accra","Haiti": "Port-Au-Prince",
   "Honduras": "Tegucigalpa","Hungary": "Budapest", "India": "New Delhi","Indonesia": "Jakarta", "Iran": "Tehran",
   "Iraq": "Baghdad","Israel": "Jerusalem","Italy": "Rome","Jamaica": "Kingston","Japan": "Tokyo",
   "Kenya": "Nairobi","Latvia": "Riga","Liberia": "Monrovia","Luxembourg": "Luxembourg","Mexico": "Mexico City",
   "Netherlands": "Amsterdam","Nigeria": "Abuja","Norway": "Oslo","New Zealand": "Wellington","Oman": "Muscat",
   "Panama": "Panama City","Poland": "Warsaw","Portugal": "Lisbon","Qatar": "Doha","Rwanda": "Kigali",
   "Russia": "Moscow","Serbia": "Belgrade","South Korea": "Seoul","Spain": "Madrid","Ukraine": "Kiev"
}

play_game = True
print("You have 3 chances to get it right\n")
while play_game:
    #get a random country from the dictionary
    country_name = choice(list(countries.keys()))
    #print("You have 3 chances to get it right\n")
    print(f"What is the capital city of {country_name}")
    #get user_input
    user_input = input(">").strip().lower()
    #chance = 1
    while user_input != countries.get(country_name).lower():
            print("You guessed wrong, try again")
            user_input = input(">").strip().lower()
            #chance = chance + 1
            
    print(f"Correct!!!")
    print("Do you want to play again: (yes/no)")
    user_response = input(">").strip().lower()
    while user_response not in ["yes","y","no","n"]:
        user_response = input("Do you want to play again: (yes/no)").strip().lower()

    if user_response == "no" or user_response =="n":
            print("Goodbye......")
            play_game = False


