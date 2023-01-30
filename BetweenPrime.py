# Taking user input for upper and lower bounds
n1 = int(input("Enter First Number "))
n2 = int(input("Enter Second Number "))

# Creating a list of primes
lp = []

# While loop to append all prime numbers between n1 and n2
while (n1 <= n2):
    count = 0
    for i in range(1, n1):
        if n1%i == 0:
            count = count+1
        else:
            continue
    if count == 1:
        lp.append(n1)
    n1 = n1+1

# Printing out the prime numbers
for j in lp:
    print(j," ")