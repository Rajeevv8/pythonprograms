n=int(input("Enter a number:"))
b=len(str(n))

reverse=0
sm=0
while(n>0):
    rem=n%10
    
    reverse=(reverse* 10)+rem
    
    sm+=(n%10)
    
    n//=10

print(reverse)
print(sm)
