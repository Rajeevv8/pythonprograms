
'''count=0
for i in range(1,a+1):
    if(i>1):
        
        for j in range(2,a):
            if(i%j==0):
                break
        else:
            print(i)'''
a=int(input("Enter the end of digits:"))                
for i in range(1, a+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            print()
        else:
            print(i)


