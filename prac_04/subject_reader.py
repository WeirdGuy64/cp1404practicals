"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)
    display_subject_details(data)


def display_subject_details(data):
    max_lecturer_name_length = max(len(element[1]) for element in data)
    for element in data:
        print(f"{element[0]} is taught by {element[1]:<{max_lecturer_name_length}} and has {element[2]:>3} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    lists = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        lists.append(parts)
        print("----------")
    input_file.close()
    return lists


main()
