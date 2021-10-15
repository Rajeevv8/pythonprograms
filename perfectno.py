a=int(input("Enter a number"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum+=i
if(sum==a):
    print("Perfect number")
else:
    print("Non perfect number")
                
    
