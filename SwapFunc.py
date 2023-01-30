f=open("sample.txt","r+")
all=f.readlines()
print("Original list is: ",all)
for i in range(len(all)):
    a=all[i].split("\n")
    f.writelines(a)
f.close()

f=open("sample.txt","r")
all=f.readlines()
print("Updated list is: ",all)
f.close()
