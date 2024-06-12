name = input("What is your name? ")
game = input("Do you want to play this treasure seeking game? (Yes/No): ").lower()
if game == "yes":
    print(f"Welcome to the Treasure Island {name} and goodluck in trying to find the treasure..")
else:
    quit()    

answer = input("You are at a crossroad and you can either turn left or right. where do you want to turn to? (left/right): ").lower()
if answer == "left":
    next = input("You come accross a river, do you want to walk round it or swim across it? (walk/swim): ").lower()
    
    if next == "walk":
        meet = input("You meet a stranger, would you like to talk to him? (yes/no): ")
        if meet == "yes":
            print("The stranger is the guard to the treasure island!!")
            key = input("you can either steal the key or ask for it, do you want to steal or ask for it. (steal or ask): ").lower()
            if key == "ask":
                print(f"The guard happily hand over the keys to you and you are now the heir of the treasure. YOU WIN!!!!")
            
            elif key =="steal":
                print("The stranger happens to be the guard of fthe treasure. He notices that you stole the key and locks you up. YOU LOSE!!") 
            
            else:
                print(f"That is an invalid input {name}, You Lose!!")       
    
    elif next == "swim":
        next = input("You are now on the other side of the river. Do you want to proced to the mountains or go back? (proceed/back): ").lower()
        if next == "proceed":
            print("It's a dead end. You were so close but you lose!!")
            
        elif next == "back":
            print("as soon as you got back to the water, you got injured badly by an aligator. you lose!!")
            
        else:
            print(f"that was an invalid input {name}. You lose!!")        
    
    else:
        print(f"That was an invalid input {name}, you lose!!")            

elif answer == "right":
    house = input("You've reached a palacial house that seems not to have anyone, would you like to continue walking or do you want to search for the treasure in the house? (walk/search): ").lower()
    if house == "walk":
        meet = input("You meet a stranger, Would you like to talk to him? (yes/no)").lower()
        if meet == "yes":
            print("The stanger misleads you and you end up at a dead end. You lose!!")
        
        elif meet == "no":
            print("The stranger get angry and decides to take you captive, you lose!!!")
            
        else:
            print(f"That was an invalid choice {name}. You lose!!!")        

    elif house == "search":
        print("Yuo've been caught by the guard and charged for theft. You lose!!")
        
    else:
        print(f"Thats an invalid input {name}. YOu lose!!!")    
else:
    print(f"Thats an invalid move {name} you lose!!")    

