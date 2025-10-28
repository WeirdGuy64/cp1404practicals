"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_subject_data(FILENAME)
    print(subject_data)
    display_subject_details(subject_data)


def display_subject_details(subject_data):
    max_lecturer_name_length = max(len(subject[1]) for subject in subject_data)
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]:<{max_lecturer_name_length}} and has {subject[2]:>3} students")


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        subject_parts = line.split(',')  # Separate the data into its parts
        print(subject_parts)  # See what the parts look like (notice the integer is a string)
        subject_parts[2] = int(subject_parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(subject_parts)  # See if that worked
        subjects.append(subject_parts)
        print("----------")
    input_file.close()
    return subjects


main()
