# Taking User Input
x = int(input("Enter Nubmer "))

# Initializing Sum for Reverse Number
s = 0

# Code to Reverse
while x!= 0:
    d = x%10
    s = s*10 + d
    x = x//10
print("Reversed Number is ",s)