# 1.
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
print(f"Hi {in_file.read(len(name))}!")
in_file.close()
