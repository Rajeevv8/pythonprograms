for i in range(5):  
    for j in range(5):
        if(i+j==4):
            print("*",end=" ")
        elif(i==0 and (j in [0,1,2,3,4])):
            print("*",end=" ")
        elif(i==5 and (j in [0,1,2,3,4])):
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()  
