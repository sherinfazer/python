
st1=input("Enter any String:")
vowels=['a','e','i','o','u','A','E','I','O','U']
flag=0
for x in st1:
	if x in vowels:
		flag=1
if(flag==1):
	print("Vowels is present")
else:
	print("Vowels is not presented")
