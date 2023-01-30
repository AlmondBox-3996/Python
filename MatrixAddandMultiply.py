# DEFINING LIST FOR MATRIX 1
r1 = int(input("Number of Rows: "))
c1 = int(input("Number of Columns: "))
lm1 = []

# LOOP FOR IMPORTING ELEMENTS
# COLUMN LOOP
for i in range(c1):
    lr = []
    # ROW LOOP
    for j in range(r1):
        x = int(input("Enter Element: "))
        lr.append(x)
    lm1.append(lr)

# DEFINING LIST FOR MATRIX 2
r2 = int(input("Number of Rows: "))
c2 = int(input("Number of Columns: "))
lm2 = []

# LOOP FOR IMPORTING ELEMENTS
# COLUMN LOOP
for i in range(c2):
    lr = []
    # ROW LOOP
    for j in range(r2):
        x = int(input("Enter Element: "))
        lr.append(x)
    lm2.append(lr)

# DISPLAYING MATRIX 1
print("Matrix 1:")
for i in range(c1):
    print(lm1[i])

# DISPLAYING MATRIX 2
print("Matrix 2:")
for i in range(c2):
    print(lm2[i])

# MENU FOR ADDITION AND MULTIPLICATION
print('''
Choose Choice of Operation
1. Matrix Addition
2. Matrix Multiplication''')

ch = int(input("Enter Choice Number: "))

# MATRIX ADDITION
if ch == 1:
    ls = []
    # CHECKING CONDITION FOR ADDITION
    if len(lm1) == len(lm2):
        if len(lm1[0]) == len(lm2[0]):
            for i in range(len(lm1)):
                lr = []
                for j in range(len(lm1[0])):
                    # ADDING ELEMENT OF MATRIX 1 WITH CORRESPONDING ELEMENT OF MATRIX 2
                    x = lm1[i][j] + lm2[i][j]
                    lr.append(x)
                ls.append(lr)
        print("Matrix Sum:")
        for i in range(len(ls)):
            print(ls[i])
    else:
        print("MATRIX ADDITION NOT POSSIBLE")
    
# MATRIX MULTIPLICATION
if ch == 2:
    lm = []
    # CHECKING CONDITION FOR MULTIPLICATION
    if len(lm1) == len(lm2[0]):
        for i in range(len(lm1)):
            lr = []
            for j in range(len(lm2[0])):
                s = 0
                for k in range(len(lm2)):
                    x = lm1[i][j]*lm2[k][i]
                    s += x
                lr.append(s)
            lm.append(lr)
        print("Matrix Product:")
        for i in range(len(lm)):
            print(lm[i])
    else:
        print("MATRIX MULTIPLICATION NOT POSSIBLE")