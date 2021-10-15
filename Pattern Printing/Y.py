for i in range(5):
    for j in range(5):
        if((i+j==4) or (i==j and (i<3) and (i<3))):
            print("#", end=" ")
           
        else:
            print(" ", end=" ")
    print()        
