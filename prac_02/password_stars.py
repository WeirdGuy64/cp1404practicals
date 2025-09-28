MINIMUM_LENGTH = 4

password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must have at least {MINIMUM_LENGTH} characters")
    password = input("Password: ")
for i in range(len(password)):
    print("*", end="")
