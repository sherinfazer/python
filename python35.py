str=raw_input("Enter str:")
count1=0
count2=0
for i in str:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The num of digits is:")
print(count1)
print("The num of characters is:")
print(count2)
