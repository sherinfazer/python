p=int(input("Enter number:"))
temp=p
rev=0
while(p>0):
    dig=p%10
    rev=rev*10+dig
    p=p//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
