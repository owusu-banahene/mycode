#!/usr/bin/env python3
import os

def readFizz():
    os.chdir("/home/student/mycode/challenger_folder")
    fizzList=list()
    with open("numfile.txt","r") as fizzfile:
        fizzList = fizzfile.readlines()
    return fizzList

def computeBuzz(buzzList):
    fizzes=buzzes=fizzBuzzes=0
    #buzzes=0
    #fizzBuzzes=0
    for number in buzzList:
        number = number.rstrip("\n")
        value = int(number)
        if value%3 == 0 and value%5 == 0:
            fizzBuzzes += 1
            print("FizzBuzz")
        elif value%3 == 0:
            fizzes += 1
            print("Fizz")
        elif value%5 == 0:
            buzzes += 1
            print("Buzz")
        else:
            print(value)
    print(f"There are {fizzes} fizzes, {buzzes} buzzes and {fizzBuzzes} fizzBuzzes")

def main():
    computeBuzz(readFizz())

if __name__== "__main__":
    main()

