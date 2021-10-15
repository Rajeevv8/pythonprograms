a=input("ENter a line")
b=a.split(" ")
c=input("Enter starting letters")
for i in b:
    if(i.startswith(c)):
        print(i)
