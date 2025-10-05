# 1.
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
print(f"Hi {in_file.read(len(name))}!")
in_file.close()

# 3.
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
    print(result)

# 4.
with open("numbers.txt", "r") as in_file:
    total = 0
    file = in_file.readlines()
    for line in file:
        total += int(line)
    print(total)
