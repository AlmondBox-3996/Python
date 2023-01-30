t = True
while t == True:
    x = int(input("Enter a number "))
    f = 0
    for i in range(2, x):   
        if x%i == 0:
            f += 1
            break
        else:
            continue
    if  f >= 1:
        a = 1
        for i in range(1,x+1):
            a = a*i
        print("Not a prime number, factorial is ",a)
    else:
        print("Prime Number")
    y = int(input("Continue??(0-n/1-y) "))
    if y == 0:
        t = False
    if y == 1:
        t = True