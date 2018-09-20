lower = 900
upper = 1000

print("Prime numbers between",lower,"and",upper,"are:")

for number in range(lower,upper + 1):
   if number > 1:
       for i in range(2,number):
           if (number % i) == 0:
               break
       else:
           print(number)
