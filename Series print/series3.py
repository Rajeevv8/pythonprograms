'''9 11 33 13 15 33 17'''
a=int(input("Enter the first number:"))
b=int(input("Enter number of terms to be added:"))
for i in range(b+1):
    if(i%2==0):
        print(a,end=" ")
    else:
        print(a,33,end=" ")
    a=a+2  
    
        
