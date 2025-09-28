MENU = """G - Get a valid score (0-100)
P - Print result
S - Show stars
Q - Quit"""


def main():
    score = int(input("Score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score (0-100): "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Score (0-100): "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Score (0-100): "))
        elif choice == "P":
            if score < 0 or score > 100:
                print("Invalid score")
            elif score >= 90:
                print("Excellent")
            elif score >= 50:
                print("Passable")
            else:
                print("Bad")
        elif choice == "S":
            for character in range(score):
                print("*", end="")
        else:
            print("That is not an option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


main()
