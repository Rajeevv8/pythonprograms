for i in range(5):
    for j in range(5):
        if((i==j) or (j==0 and i<5) or (i==4 and j<5) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    
