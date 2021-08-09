#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def characters(data,chara_num):
    allegiances = data["allegiances"]
    books = data["books"]
    povBooks = data["povBooks"]
    name = data["name"] or data["aliases"][0]
    print(f"""Details of Character: {chara_num}""")
    print(f'Name :{name}')
    print("Houses:")
    if len(allegiances)>0:
        for house in allegiances:
            print(requests.get(house).json()['name'])
    else:
        print('No Allegiance')
    print()
    if len(books) > 0:
        print("Books:")
        for book in books:
            print(requests.get(book).json()['name'])
    else:
        print("No Books")
    print()
    if len(povBooks)> 0:
        print("Point of View books:")
        for pov in povBooks:
            print(requests.get(pov).json()['name'])



def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #pprint.pprint(got_dj)
        characters(got_dj,got_charToLookup)

if __name__ == "__main__":
        main()

