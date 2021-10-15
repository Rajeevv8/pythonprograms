a=[]
x=int(input("Enter rowsize:"))
y=int(input("Enter colsize:"))
for i in range(x):
    a.append([])
    for j in range(y):
        a[i].append(int(input("Enter elements:")))

for i in range(x):
    for j in range(y):
        print(a[j][i],end=" ")
        
    print()
