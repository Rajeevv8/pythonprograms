x=input("Enter a string").strip()
count=0
count1=0
count2=0
count3=0
vow=['a','e','i','o','u','A','E','I','O','U',]
cha=['!','@','$','&','*']
for i in range(len(x)):
    if(x[i] in vow):     
        count+=1
    elif(x[i] in cha):
        count1+=1
    elif(x[i].isnumeric()):
        count2+=1
    elif(x[i] not in vow and x[i]!=" "):
        count3+=1
        
print("Vowels:",count)
print("Special:",count1)
print("Numbers:",count2)
print("Consonants:",count3)
