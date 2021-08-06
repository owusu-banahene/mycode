#!/usr/bin/env python3
#import libraries
import os
import requests
from random import shuffle

def presentQuestion(question,questionNumber):
    answers = list()
    sampleQuestion = question["question"]
    correct = question["correct_answer"]
    answers.insert(0,correct)
    incorrect = question["incorrect_answers"]
    answers.extend(incorrect)
    #shuffle multiple choice
    shuffle(answers)
    crossCheck={"a":answers[0],"b":answers[1],"c":answers[2],"d":answers[3]}
    print(f"{questionNumber}). {sampleQuestion}")
    print(f"""\tA.{answers[0]}
        B.{answers[1]}
        C.{answers[2]}
        D.{answers[3]}      
              """)

    response = input("Choose A, B,C, or D > ").strip().lower()
    if response in ["a","b","c","d"]:
        if crossCheck.get(response) == correct:
            print("correct")
        else:
            print("wrong")
    else:
        print("Invalid Input")
          


def data():
    trivial_data=dict()
    questionNumber =0
    API = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
    response = requests.get(API)
    questions = response.json()
    print(""" Welcome to the trivial game

              You will be presented with 10 mulitple choice questions 
              
              """)
   
    for question in questions.get("results"):
        questionNumber += 1
        presentQuestion(question,questionNumber)
        

def main():
   data()

if __name__ =="__main__":
    main()
