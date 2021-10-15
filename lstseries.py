'''a=int(input("Enter the number of digits to be added to the series"))'''

x=int(input("Start of odd places:"))
y=int(input("Start of even places:"))
z=int(input("Enter the length of the list:"))
lst=[x,y]

for i in range(0,z):
    
    
    if(lst[i]%2==0):
        lst.append(lst[i]+1)        
    elif(lst[i]%2==0):
        lst.append(lst[i]+1)

print(lst)        
