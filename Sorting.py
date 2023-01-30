l = []
x = 1
while x == 1:
    i = int(input("Enter list element: "))
    l.append(i)
    c = input("Do you want to continue [y/n]: ")
    if c == "y":
        x = 1
    elif c == "n":
        x = 0
    else:
        print("Invalid Entry")
print("list before sorting",l)
l.sort()
print("list after sorting",l)