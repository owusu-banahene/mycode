#!/usr/bin/env python3
from random import randint
#ice cream flavor list
icecream=["flavors","salty"]
#student's name
tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]
#append 99 to flavor list
icecream.append(99)
#get an integer between 0 and 19 inclusively
user_input = input("Enter an integer value between 0 and 19 inclusively: ")
print(f"{icecream[-1]} {icecream[0]}, and {tlgclass[int(user_input)]} chooses to be {icecream[1]}.")
print("Randomly generated person")
print(f"{icecream[-1]} {icecream[0]}, and {tlgclass[randint(0,19)]} chooses to be {icecream[1]}.")
