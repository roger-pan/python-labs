'''
Code a game of rock paper scissors.

'''


# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand ==2:
        return "paper"

    # for example if the variable hand is 0, it should return the string "scissor"
print(get_hand(1))

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer==2 and player == 0):
        return "You won!"
    elif computer == player:
        return "You tied!"
    else:
        return "You won!"




'''
Start here
'''

# take in a number 0-2 from the user that represents their hand
player = int(input("Input a number between 0 and 2: "))

# generate a random number 0-2 to use for the computer's hand
import random
computer = random.randint(0,2)

# call the function get_hand to get the string representation of the user's hand
player_hand = get_hand(player)

# call the function get_hand to get the string representation of the computer's hand
computer_hand = get_hand(computer)

# call the function determine_winner to figure out the winner
winner = determine_winner(computer,player)

# print out the player hand and computer hand
print(player_hand)
print(computer_hand)

# print out the winner
print(winner)