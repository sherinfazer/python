lst1 = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst1.append(numbers)
print(max(lst1), "\nMinimum element in the list is :", min(lst1))
