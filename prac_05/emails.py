"""
Emails
Expected time: 15 minutes
Actual time: 42 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ")
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email"""
    email_extraction_part_one = email.split("@")[0]
    email_extraction_part_two = email_extraction_part_one.split(".")
    name = " ".join(email_extraction_part_two).title()
    return name


main()
