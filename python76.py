no=int(input("Enter any number"))
flag=0
for x in range(1,no+1):
	if(no%x==0):
		flag=flag+1
if(flag>2):
	print1("composite")
else:
        print("Not composite")
