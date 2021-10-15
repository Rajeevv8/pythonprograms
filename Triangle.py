
for i in range(5):
    for j in range(5):
        if(j==0 or i==j or((i==5) and (j in [0,1,2,3,4]))):
            print("+",end=" ")
            
        else:
            print(" ",end=" ")
    print()
