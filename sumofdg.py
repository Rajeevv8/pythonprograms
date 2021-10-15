a=[]
dg=[]
sm=0
x=int(input("Rowsize:"))
y=int(input("Colsize:"))
for i in range(x):
    a.append([])
    for j in range(y):
        a[i].append(int(input("Element:")))
        if(i==j):
            dg.append(a[i][j])
        
        
            
print(a)    
for i in dg:
    sm+=i
print(sm)
