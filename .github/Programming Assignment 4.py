# Programmers: Anthony DelVecchio
# Date: 11/10/21
# Programming Assignment: 4
# Program Inputs: Whether or not the player would like to draw or stand
# Program Outputs: Determines whether or not the player wins or loses

# Import Random
import random
# Dealer Cards
dealer_cards = []
# Player Cards
player_cards = []
# Deal cards to dealer
def deal_cards_dealer():
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has ", dealer_cards)
def deal_cards_player():
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have ", player_cards)
# Define main function
def main():
    deal_cards_dealer()
    deal_cards_player()
    while sum(player_cards) < 21:
        action_taken = str(input("Do you want to stay or hit? "))
        action_taken = action_taken.strip().lower()
        if action_taken == "hit":
            player_cards.append(random.randint(1, 11))
            print("You now have a total of " + str(sum(player_cards)) + " from these cards", player_cards)
        elif action_taken == "stay":
            print("The dealer has a total of " + str(sum(dealer_cards)) + " with", dealer_cards)
            print("You have a total of " + str(sum(player_cards)) + " with", player_cards)
        else:
            print("Invalid Input")
            main()
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
            exit()
        elif sum(dealer_cards) < sum(player_cards):
            print("You win!")
            exit()
        if sum(player_cards) > 21:
            print("You busted! Dealer Wins!")
            exit()
        elif sum(player_cards) == 21:
            print("You have Blackjack! You win!")
            exit()
# Run code
main()