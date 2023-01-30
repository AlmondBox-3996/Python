# Initialising Terms
l = []
lnew = []

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

# Replacing Last Term
p = int(input("Enter New Element "))
for i in range(n):
    temp = list(l[i])
    temp.pop(-1)
    temp.append(p)
    t = tuple(temp)
    lnew.append(t)
print(l)
print(lnew)