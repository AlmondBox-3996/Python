# Initiallizing Terms
l = []
p = 1

# Creating Tuple
n = int(input("Enter Number of Terms "))
for i in range(n):
    x = int(input("Enter term "))
    l.append(x)
t = tuple(l)

# Multiplying Terms of Tuple
for i in t:
    p = p*i
print("Product is ",p)