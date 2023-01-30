# Loop for Number of Rows
for i in range(1,8):

    # Conditon to Print First 4 Rows
    if i <= 4:
        # Row Elements
        for j in range(i):
            print('*',end=' ')
            j += 1
    
    # Condition to Print Last 3 Rows
    else:
        # Row Elements
        for j in range(8-i):
            print('*',end=' ')
            j += 1
    
    # Iteration to Next Row
    print()
    i += 1