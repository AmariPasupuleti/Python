import random

def roll():
    roll=random.randint(1,6)
    return roll

while True:
    players=input('Enter the number of players (2-4): ')
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be b/w 2-4 players")
    else:
        print("Invalid Try again")

max_score=30
player_scores=[0 for j in range(players)]
print(player_scores)

while max(player_scores)< max_score:
    for player_index in range(players):
        print("\nPlayer Number",player_index+1,"just started their turn")
        print("Your Total Score is",player_scores[player_index],"\n")
        current_score=0
        
        while True:
            should_roll=input("\nWolud you like to roll (y)? ")
            if should_roll.lower()!='y':
                break
            value=roll()
            if value==1:
                print("\nYou rolled a 1! Turn Done! \n")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a : ",value)
            print("Your score is:",current_score)
        player_scores[player_index]=current_score
            
max_score=max(player_scores)
winner=player_scores.index(max_score)
print("\nPlayer number",winner+1,"Win this game!")
        
        