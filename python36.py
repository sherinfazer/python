str = input("Please Enter your Own Str : ")
alphabets = digits = special = 0

for i in range(len(str)):
    if(str[i].isalpha()):
        alphabets = alphabets + 1
    elif(str[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Num of Alphabets in this Str :  ", alphabets)
print("Total Num of Digits in this Str :  ", digits)
print("Total Num of Special Characters in this Str :  ", special)

