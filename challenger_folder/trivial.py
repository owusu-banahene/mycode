#!/usr/bin/env python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import requests
from random import shuffle

app = Flask(__name__)
API="https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"
#app = Flask(__name__)

@app.route("/")
def index():
    solutions=[]
    response = requests.get(API).json()
    questions = response.get("results")["question"]
    correct = response.get("results")["correct_answer"]
    solutions.append(correct)
    incorrect = response.get("results")["incorrect_answers"]
    solutions.extend(incorrect)
    shuffle(solutions)
    answers={'a':solutions[0],'b':solutions[1],
            'c':solutions[2],'d':solutions[3]}
    return render_template("questions.html",question=questions,answers=answers,soln=correct)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
