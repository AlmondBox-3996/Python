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

# Determinant Finding
for i in lm[0]:
    lm[1][]