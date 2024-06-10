print("Welcome to my compuer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play then :) ")
score = 0

answer = input("What does CPU stand for? ").lower()
canswer = "central processing unit".lower()
if answer == canswer:
    print("Correct!")
    score += 1

else:
    print(f"Incorrect! The answer is {canswer}.")    
    
answer = input("What is the chemical symbol for gold ").lower()
canswer = "Au".lower()
if answer == canswer:
    print("Correct!")
    score += 1

else:
    print(f"Incorrect! The answer is {canswer}.")

answer = input("What is the tallest mountain in the world? ").lower()
canswer = "Mount Everest".lower()
if answer == canswer:
    print("Correct!")
    score += 1

else:
    print(f"Incorrect! The answer is {canswer}.")

answer = input('Who is known as the "Father of Modern Physics"? ').lower()
canswer = "Isaac Newton".lower()
if answer == canswer:
    print("Correct!")
    score += 1

else:
    print(f"Incorrect! The answer is {canswer}.")

answer = input("What is the largest planet in our solar system? ").lower()
canswer = "Jupiter".lower()
if answer == canswer:
    print("Correct!")
    score += 1

else:
    print(f"Incorrect! The answer is {canswer}.")   
    
percentage = (score/5)*100
print(f"You got {percentage}%")
print(f"You got {score} questions correct")
  
                