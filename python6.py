E = int(input("Enter E: "))
if E % 4 == 0 and year % 100 != 0:
    print(E, "is a Leap Year")
elif E % 100 == 0:
    print(E, "is not a Leap Year")
elif E % 400 ==0:
    print(E, "is a Leap Year")
else:
    print(E, "is not a Leap Year")
