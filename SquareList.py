l = [1,2,3]
print(l)
for i in l:
    c = l.index(i)
    l[c] = i**2
print(l)