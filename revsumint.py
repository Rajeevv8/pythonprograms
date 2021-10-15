n=int(input("Enter a number:"))
b=len(str(n))
reverse=0
sm=0
for i in range(b):
    rem=n%10
    print("Rem",rem)
    reverse=(reverse*10)+rem
    print("Rev",reverse)
    sm+=(n%10)
    print("Sum",sm)
    n//=10

print(reverse)
print(sm)
