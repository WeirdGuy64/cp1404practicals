"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(return_result(score))
    random_score = randint(0, 100)
    print(return_result(random_score))


def return_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
