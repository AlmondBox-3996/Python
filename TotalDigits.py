# Recieving User Input
x = int(input("Enter Number "))

# Initializing Count
c = 0

# Incrementing Count
while x != 0:
    c = c+1
    x = x//10
print("Total number of digits is ",c)