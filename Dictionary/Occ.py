name=input("Enter name:")
for i in set(name):
    print({i:name.count(i)})