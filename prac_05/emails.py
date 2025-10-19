"""
Emails
Expected time: 15 minutes
Actual time:
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        print(name)
        email = input("Email: ")


def extract_name(email):
    """Extract name from email"""
    email.split("@")
    if "." in email:
        email.split(".")
        list(email[0, 1]).join()
    return email[0]


main()
