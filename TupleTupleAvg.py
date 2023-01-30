# Initialising Terms
l = []

# Creating Tuple of Tuples
n = int(input("Enter Number of Tuples "))
tn = int(input("Enter Number of Elements per Tuple "))
for i in range(n):
    lt = []
    for j in range(tn):
        x = int(input("Enter Element "))
        lt.append(x)
    tt = tuple(lt)
    l.append(tt)
t = tuple(l)

# Calculating Average Tuple
avg = []
for i in range(n):
    s = 0
    for j in range(tn):
        s = s+t[i][j]
    avg.append(s/tn)
avgt = tuple(avg)
print(t)
print(avgt)