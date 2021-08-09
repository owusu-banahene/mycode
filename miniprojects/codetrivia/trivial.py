#!/usr/bin/env python3
#import libraries
import os
import requests
from random import shuffle


def presentQuestion(question,questionNumber):
    answers = list()
    correct_answer = False
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
    response =""
    while response not in ["a","b","c","d"]:
        #print("Invalid input")
        response = input("Choose A, B,C, or D > ").strip().lower()
    if response in ["a","b","c","d"]:
        if crossCheck.get(response) == correct:
            print("correct")
            correct_answer = True
        else:
            print("wrong")
        
    return correct_answer


def data(categoryId,level):
    trivial_data=dict()
    questionNumber =0
    score = 0
    API = f"https://opentdb.com/api.php?amount=10&category={categoryId}&difficulty={level}&type=multiple"
    response = requests.get(API)
    questions = response.json()
    if len(questions.get("results")):
        print(""" Welcome to the trivial game

                  You will be presented with 10 mulitple choice questions 
                  
                  """)
       
        for question in questions.get("results"):
            questionNumber += 1
            if presentQuestion(question,questionNumber) == True:
                score += 1
    else:
        print("Sorry, we dont have questions under this category and difficulty level") 
        score = -1
    return score

category ={
        "general knowledge":9,"book":10,"film":11,"music":12,"musicals and theatres":13,"television":14,"video":15,
        "board games":16,"science and nature":17,"computers":18,"mathematics":19,"mythology":20,"sports":21,
        "geography":22,"history":23,"politics":24,"art":25,"celebrities":26,"animals":27,"vehicels":28,
        "comics":29,"gadgets":30,"japanese anime and manga":31,"cartoons and animations":32
        }

def main():
   #correct_answers =0
   play = True
   while play:
       print(f'Choose the category from the list {[*category]}:')
       game_category = input(">").strip().lower()
       print("Choose the level of difficulty from the list [easy,medium,hard]: ")
       game_difficulty = input(">").strip().lower()
       scored_value = data(category.get(game_category),game_difficulty)
       if scored_value != -1:
           print(f"Your score was {scored_value} out of 10")
           print("Do you want to continue with the game? (Yes/No)")
           user_response = ""
           while user_response.lower() not in ["yes","y","no","n"]:
               user_response = input(">").strip().lower()
           if user_response in ["no","n"]:
                play= False


if __name__ =="__main__":
    main()
