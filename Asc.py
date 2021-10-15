a=int(input("Enter a Number:"))
b=int(input("Enter next Number:"))
c=int(input("Enter next Number:"))
d=a+b
e=b+c
f=a+c
g=a & b
h=b & c
i=c & a
list1=[a,b,c,d,e,f,g,h,i]
x=max(list1)
ans=sorted(list1)
ans2=list(reversed(ans))
print(x,"\n",ans,"\n",ans2)


