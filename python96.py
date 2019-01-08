
number=int(input("Enter any number"))
j=0
for x in range(1,number+1):
	if(number%x==0):
		j=j+1
if(j>2):
	print("composite")
else:
        print("Not composite")
