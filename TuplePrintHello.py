# Creating tuple
tuple1=(1,2,3,4,5)
print(tuple1)

# Converting to list and appending "hello"
list1=list(tuple1)
list1.append('hello')

# Reconverting from list to tuple
tuple1=tuple(list1)
print(tuple1)