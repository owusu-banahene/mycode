#!/usr/bin/env python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import requests
from random import shuffle
from flask import make_response

app = Flask(__name__)
API="https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"
#app = Flask(__name__)

@app.route("/correct")
def success():
    return f"That is correct!"


@app.route("/checks", methods = ["POST"])
def login():
        if request.json:
            data= request.json
            if data["chosen_answer"] == 42:
                return redirect("/correct")
            else:
                return redirect("/")

        if request.form.get("chosen_answer"):
            answer = request.form.get("chosen_answer")
            solution = request.form.get("hidden")
            if answer.lower() == solution.lower():
                return redirect("/correct")
            else:
                return redirect("/")
        else:
            return redirect("/")

@app.route("/")
def index():
    solutions=[]
    response = requests.get(API).json()
    questions = response.get("results")[0]["question"]
    correct = response.get("results")[0]["correct_answer"]
    solutions.append(correct)
    incorrect = response.get("results")[0]["incorrect_answers"]
    solutions.extend(incorrect)
    shuffle(solutions)
    answers={'a':solutions[0],'b':solutions[1],
            'c':solutions[2],'d':solutions[3]}
    return render_template("questions.html",question=questions,answers=answers,soln=list(answers.keys())[list(answers.values()).index(correct)])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
