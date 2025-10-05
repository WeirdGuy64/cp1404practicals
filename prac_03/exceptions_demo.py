"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Answers:
1. When the numerator or the denominator inputs are not integers
2. When the denominator input is 0
3. You could add an if statement that detects if the user inputs 0 and stop the calculation if an input of 0 is detected, but I think it would quicker and easier to just use exceptions
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
