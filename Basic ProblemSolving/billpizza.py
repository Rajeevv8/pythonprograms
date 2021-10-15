bill=0
a=int(input("Choose What type of pizza\n1:Small\n2:Medium\n3:Large"))
if(a==1):
    bill+=20
elif(a==2):
    bill+=30
else:
    bill+=50
b=int(input("Choose if you want toppings\n4:Yes\n5:No"))
if(b==4 and a==1):
    bill+=10
if(b==4 and a==2):
    bill+=20
elif(b==4 and a==3):
    bill+=30
else:
    bill+=0
c=int(input("Do you want cheese?\n6.Yes\n7.No"))
if(b==6):
    bill+=10
else:
    bill+=0
print("Please pay:",bill)    
