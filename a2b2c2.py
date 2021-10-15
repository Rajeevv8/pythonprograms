x=input("Enter string:")
for i in range(0,len(x),2):
    if(x[i].isalpha()):
        print(x[i]*int(x[i+1]),end="")
    else:
        print(int(x[i])*x[i+1],end="")
    
        
        
