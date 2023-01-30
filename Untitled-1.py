str = input("Enter string ")
rep = input("Enter word to be replaced ")
wor = input("Enter word to replace with ")
l = str.split(' ')
fstr = ''
print(l)
for i in l:
    if i == rep:
        ind = l.index(i)
        l.remove(i)
        l.insert(ind,wor)
print(l)
for i in l:
    fstr = fstr + i + ' '
print(fstr)