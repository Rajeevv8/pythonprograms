para=input("Enter a para:")
x=para.split()
word=input("Enter word start")
for i in x:
    if(word==i[0:len(word)]):
        print(i)
