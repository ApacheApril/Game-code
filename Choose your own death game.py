name = input("Type your name: ")
print("Welcome to the game", name, ":)")

answer = input("You wake up in a dark room, there are two lit up doors to the left and right, which door do you choose? ").lower()

if answer == "left":
    answer = input("You meet a wounded unconscious boy near the entrance. Do you want to wake him up or run away? ").lower()
    
    if answer == "wake him up":
        print("You woke him up but he screamed and ran further down the corridor, do you want to chase him or leave him? ").lower()
        
        if answer == "chase him":
            print("He runs into the dark corridor screaming for help and eventually he runs into a pit , Do you want to try to save him or leave him").lower()
            
        elif answer == "leave him":
            print()
    
    elif answer == "run away":
        print("You left him and ran further down the corridor until you fell in a pit and died. You could've been so much more...")
        quit()
    
    else:
        print("This isn't your game...")
        quit()
    
    
elif answer == "right":
    answer = input("You meet a wounded unconscious girl near the entrance. Do you want to wake her up or run away? ").lower()
    
    if answer == "wake her up":
        print("She introduces herself as Maya, do you want to search with her or go alone? ").lower
        
        if answer == "search with her":
            print()
        
        elif answer == "go alone":
            print()
    
else:
    print("This isn't your game...")
    quit()