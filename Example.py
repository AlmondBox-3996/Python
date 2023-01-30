i = 0
n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
for i in range(0,101,5):
    while i!=1:
        n = 0
        if i%2 == 0:
            i = i//2
            n += 1
        else:
            i = 3*i + 1
            n += 1
    if n%10 == 0:
        n0 += 1
    elif n%10 == 1:
        n1 += 1
    elif n%10 == 2:
        n2 += 1
    elif n%10 == 3:
        n3 += 1
    elif n%10 == 4:
        n4 += 1
    elif n%10 == 5: 
        n5 += 1
    elif n%10 == 6:
        n6 += 1
    elif n%10 == 7: 
        n7 += 1
    elif n%10 == 8:
        n8 += 1
    elif n%10 == 9:
        n9 += 1
    print(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9)
