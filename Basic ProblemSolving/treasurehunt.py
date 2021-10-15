a=input("Left or Right?")
if(a=="left"):
    print("Game Over")
elif(a=="right"):
    b=input("Swim or Wait?")
    if(b=="wait"):
        print("End Game")
    elif(b=="swim"):
        c=input("What color do you choose?")
        if(c=="yellow"):
            print("You win")
        else:
            print("Game over")
