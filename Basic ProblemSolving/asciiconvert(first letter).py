a=input("Enter a string")
b=ord(a[0])
b-=32
c=chr(b)
print(c,end="")
for i in range(1,len(a)):
    print(a[i],end="")
    
