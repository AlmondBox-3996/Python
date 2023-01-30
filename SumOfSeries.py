n = int(input("Enter number in the series "))
s = 0
for i in range(1,n+1):
    a = 1/(i**2)
    s = s+a
print("Sum of Series is ",s)    