#!/usr/bin/env python3
#import libraries
import os
import requests

def data():
    trivial_data={}
    API = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
    response = requests.get(API)
    questions = response.json()
    for trivial in questions.get("results"):
            print(trivial["question"])
            print(trivial["correct_answer"])
            for each_wrong_answer in trivial["incorrect_answers"]:
                print(each_wrong_answer)

    #print(questions.keys())
    print(trivial_data)
    return trivial_data


def main():
    data()

if __name__ =="__main__":
    main()
