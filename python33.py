fname = input("Enter file name: ")
s = 0
 
with open(fname, 'o') as s:
    for line in d:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isspace):
                    m=m+1
print("Occurrences of blank spaces:")
print(m)
