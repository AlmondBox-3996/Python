# Taking User Input
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

# Displaying Arithemetic Operations and Program Termination
print('''
Enter code for operation: 
1. Addition
2. Subtraction 
3. Multiplication
4. Division
5. Quit''')

# Initialising Continuous Loop and Main Program
x = True
while x == True: 
    ch = int(input("Enter choice number "))
    if ch == 1:
        print("Sum = ", a+b)
    elif ch == 2:
        print("Difference = ", a-b)
    elif ch == 3:
        print("Product = ", a*b)
    elif ch == 4:
        print("Quotient = ", a/b)
    elif ch == 5:
        x = False
    else:
        print("Invalid input")

print("Have a nice day!")