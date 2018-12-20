fname = input("Enter file name: ")
num_lines = 0
with open(fname, 's') as n:
    for line in n:
        num_lines += 1
print("Number of lines:")
print(num_lines)
