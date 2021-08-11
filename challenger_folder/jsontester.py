#!/usr/bin/env python3
import requests
import json

API = "http://10.9.171.73:2224/checks"
print("How old are you")
answer=input("What is your answer").strip()
jsontest = {'chosen_answer':int(answer)}
requests.post(API,data=jsontest)
