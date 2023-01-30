l = [1,2,3,4,5,6,7,8,9]
print(l)
for i in l:
    if i%2 != 0 :
        c = l.index(i)
        l[c] = i**3
print(l)