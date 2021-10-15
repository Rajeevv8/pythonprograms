n=int(input("Enter a number"))
temp=n
sum=0
a=len(str(n))
while(n>0):
    rem=n%10
    sum+=rem**a
    n=n//10
    
    
if(temp==sum):
    print(f"{temp} is an armstrong number")
else:
    print(f"{temp} is not an armstrong number ")
