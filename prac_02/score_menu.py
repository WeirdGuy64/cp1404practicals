MENU = """G - Get a valid score (0-100)
P - Print result
S - Show stars
Q - Quit"""


def main():
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(return_result(score))
        elif choice == "S":
            print_stars(score)
            print()
        else:
            print("That is not an option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def print_stars(score):
    for character in range(score):
        print("*", end="")


def return_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_score():
    score = int(input("Score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score (0-100): "))
    return score


main()
