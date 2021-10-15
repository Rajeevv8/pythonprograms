a=input("Enter a name:")
b=input("Enter letter").strip()
count=0
for i in range(len(a)):
    if(a[i]==b and b!=" "):
        count+=1
print(a)        
print("Occurences:",count)        
