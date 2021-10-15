x=input("Enter string:").strip()
count=1
for i in range(len(x)-1):
    
    if(x[i]==x[i+1]): 
        count+=1
    else:
        
        print(x[i],end="")
        print(count,end="")
        count=1
        
print(x[-1]+str(count))        
