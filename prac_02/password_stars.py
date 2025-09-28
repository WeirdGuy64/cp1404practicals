MINIMUM_LENGTH = 4


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must have at least {MINIMUM_LENGTH} characters")
        password = input("Password: ")
    return password


main()
