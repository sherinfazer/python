num1=int(input("Enter number:"))
ans=''
while(num1!=0):
	t=num1%10
	if t%2!=0:
		ans=ans+' '+str(t)
	num1=num1//10
print("ODD number is",ans[::-1])
