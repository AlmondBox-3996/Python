# Initialising Terms
l = []

# Creating List of Tuples
n = int(input("Enter Number of Tuples "))
tn = int(input("Enter Number of Elements per Tuple "))
for i in range(n):
    lt = []
    for j in range(tn):
        x = int(input("Enter Element "))
        lt.append(x)
    tt = tuple(lt)
    l.append(tt)

# Calculating Average List
sum = []
for i in range(n):
    s = 0
    for j in range(tn):
        s = s+l[i][j]
    sum.append(s)
print(l)
print(sum)