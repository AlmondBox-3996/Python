# Taking User Inputs
x = int(input("Enter first number "))
y = int(input("Enter second number "))
z = int(input("Enter third number "))

# If Statements
# x is largest integer
if x > y:
    if x > z:
        print(x,"is the largest number")
    else:
        print(z,"is the largest number")

# y is largest integer
else: 
    if y > z:
        print(y,"is the largest number")
    else:
        print(z,"is the largest number")