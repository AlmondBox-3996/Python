r = int(input("Enter number of rows "))
c = int(input("Enter number of columns "))
lm = []
for i in range(c):
    lc = []
    for j in range(r):
        x = int(input("Enter element "))
        lc.append(x)
    lm.append(lc)
for k in lm:
    print(k)

mcl = []
s1 = 0
s2 = 0
for i in lm:
    s1 = s1+i[0]
    s2 = s2+i[1]
    mcl.append(s1)
    mcl.append(s2)

sigpt = []
for i in lm:
    a = [(i[0]-mcl[0])**2,(i[1]-mcl[1])**2]
    sigpt.append(a)

print(sigpt)