n = int(input("Enter the number of columns "))
x = 0
y = 0
m = 0
cf =0 
fl = []
xl = []
yl = []
cfl = []
a = int(input("Enter interval "))
for i in range(n):
    f = int(input("Enter frequency "))
    fl.append(f)
    cf = cf + f
    cfl.append(cf)
    y = y + a
    xl.append(x)
    yl.append(y)
    m = m + ((y-x)/2)*f
    x = x + a
m = m/n

print()
print("Interval","  ","Frequency","     ","CF")
for j in range(n):
    print(xl[j],"-",yl[j],"    ",fl[j],"             ",cfl[j])
print()
print("Mean is ",m)

mf = max(fl)
ind = fl.index(mf)
m2 = xl[ind]+(((fl[ind]-fl[ind-1])/((2*fl[ind])-fl[ind-1]-fl[ind+1]))*a)
print("Mode is ",m2)

mc = n/2
for k in range(n):
    if cfl[k] >= mc:
        med = xl[k]+(((mf-cfl[k])/fl[k])*a)
        break
    else:
        continue
print("Median is ",med)