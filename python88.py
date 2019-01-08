
a=int(input("enter  number"))
b=int(input("enter  number"))
for i in range(1,(a*b)+1):
    if(i%a==0 and i%b==0):
      print(i)
      break
