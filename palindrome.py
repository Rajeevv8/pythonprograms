a=int(input("Enter a number"))
b=a
rev=0
for i in range(len(str(a))):
    rev=(rev*10)+a%10
    a//=10
print(rev)    
if(b==rev):
    print("Palindrome")
else:
    print("Not a palindrome")
