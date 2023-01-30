for i in range(5):
    for j in range(i+1):
        x = chr(65+j)
        print(x,end=" ")
        if j!=i:
            print("&",end=" ")
    print()
    print()
    print()