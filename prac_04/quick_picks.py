import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_picks = int(input("How many quick picks? "))
while number_of_picks < 1:
    print("Invalid number. Please select a number higher than 0.")
    number_of_picks = int(input("How many quick picks? "))

for line in range(number_of_picks):
    numbers = []
    for i in range(NUMBERS_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:>2}" for number in numbers))
