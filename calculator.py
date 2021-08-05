#!/usr/bin/env python3

def operation(first_value,second_value,operator):
    answer = 0
    if operator == "add":
        answer = first_value + second_value
    elif operator == "subtract":
        answer = first_value - second_value
    elif operator == "divide":
        try:
            answer = first_value/second_value
        except ZeroDivisionError:
            answer=f"not possible because the divider was 0"
    elif operator == "multiply":
        answer = first_value * second_value
    return answer


def main():
    while True:
        try:
            x = float(input("Enter the first number: "))
            y= float(input("Enter the second  number: "))
            break
        except:
            print("Invalid input, try again.")

    operator = ""
    while(operator != "add" and operator != "subtract" and operator != "divide" and operator != "multiply"):
        operator = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()

    if operator in ["add","subtract","divide","multiply"]:
        print(f"The result of {x} and {y} with the {operator} operator is {operation(x,y,operator)}")
    else:
        print("use a valid OPTION")

if __name__ == "__main__":
    main()

