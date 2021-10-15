num=""
n=5
for i in range(n,0,-1):
    print("*"*(i-1),end="")
    num+=str(n+1-i)
    print(num)
    
