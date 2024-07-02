import random

# Function to simulate rolling a dice

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

# Loop to get the number of players, ensuring it is between 2 and 4

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        
        else:
            print("Must be 2-4 players.")
            
    else:
        print("Invalid, try again")

# Set the maximum score to win the game        
max_score = 50
# Initialize scores for each player
player_scores = [0 for _ in range(players)]  
 
# Main game loop, runs until a player reaches the max_score
while max(player_scores) < max_score:
    
    for i in range(players): 
        print(f"\nPlayer {i + 1} turn has just started!\n")
        print(f"Your total score is : {player_scores[i]}\n")
        current_score = 0
        
        # Loop for rolling the dice within a player's turn
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break      
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")        
                
            print(f"your score is: {current_score}")  
              
        # Update the player's total score after their turn    
        player_scores[i] += current_score
        print(f"Your total score is : {player_scores[i]}")
            
# Determine the winner by finding the player with the highest score        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player {winning_idx + 1} is the winner with a score of {max_score}")        