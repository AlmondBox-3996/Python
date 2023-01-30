# Taking User Input
a = int(input("Enter a number "))

# Checking For Divisibility
if a%7 == 0:
    print("Divisible by 7")
    if a%9 == 0:
        print("Divisible by 9")
elif a%9 == 0:
    print("Divisible by 9")
else:
    print("Not divisible by 7 or 9")