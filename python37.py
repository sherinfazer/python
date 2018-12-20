print("Enter 'y' for exit.");
num1 = input("Enter first number: ");
if num1 == 'y':
    exit();
else:
    num2 = input("Enter sec number: ");
    print("\nStarted swapping the given two numbers...");
    numbers1 = int(num1);
    numbers2 = int(num2);
    swap = numbers1;
    numbers1 = numbers2;
    numbers2 = swap;
    print("Given two numbers are successfully swapped!\n");
    print("Value of First and Sec number after swapping:");
    print("First Number =",number1,"\nSecond Number=",number2);
