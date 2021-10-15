a=int(input("Enter a number"))
fact=1
print("Every occurance:-\n")
for i in range(1,a+1):
    fact=fact*i
    '''Prints every iteration in the process'''
    print(fact)
'''Prints the total factorial'''
print("Total:",fact)    
