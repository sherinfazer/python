number1=int(input("Enter 1st number"))
number2=int(input("Enter 2nd number"))
flag=0
prod=number1*number2
for x in range(1,max(number1,number2)+1):
	k=x*x
	if k==prod:
		flag=1
if (flag==0):
	print("NO")
else:
	print("Yes")
