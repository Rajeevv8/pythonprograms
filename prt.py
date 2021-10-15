a=1
for i in range(5):
    a=1
    for j in range(5):
        if(i+j==4):
            print(a,end="")
            a+=1       
        elif(i+j==5):
            print(a,end="")
            a+=1
        elif(i+j==6):
            print(a,end="")
            a+=1
        elif(i+j==7):
            print(a,end="")
            a+=1
        elif(i+j==8):
            print(a,end="")
            a+=1     
        else:
            print("*",end="")
    print()    
