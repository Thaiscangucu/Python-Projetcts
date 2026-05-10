import random
from replit import clear
from art import logo


#Deal cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


#Calculate scores
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


#compare hands
def compare(player_score, dealer_score):

  if player_score > 21 and dealer_score > 21:
    return "You went over 21. You lose!\n"

  if player_score == dealer_score:
    return "It's a draw.\n"
  elif dealer_score == 0:
    return "You lose, delear has a blackjack!\n"
  elif player_score == 0:
    return "You win with a blackjack!\n"
  elif player_score > 21:
    return "You lose!\n"
  elif dealer_score > 21:
    return "You win! Delear went over 21\n"
  elif player_score > dealer_score:
    return "You win!\n"
  else:
    return "You lose!\n"


def start_game():

  print(logo)

  player = []
  dealer = []
  game_over = False

  #Deals 2 random cards from the deck to the user and dealer with function deal_card()
  for i in range(2):
    player.append(deal_card())
    dealer.append(deal_card())

  while not game_over:
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)
    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Dealer's first card: {dealer[0]}\n")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
      game_over = True
    else:
      user_shold_deal = input("Would you like to Hit or Stand? ").lower()
      if user_shold_deal == "hit":
        player.append(deal_card())
      else:       
        game_over = True

  while dealer_score != 0 and dealer_score < 17 and not game_over:
    dealer.append(deal_card())
    dealer_score = calculate_score(dealer)
    
  
  print(f"\nYour final hand: {player}. Your final score: {player_score}.")

  print(f"Dealer's final hand: {dealer}. Their final score: {dealer_score}\n")

  print(compare(player_score, dealer_score))


while input("Type 'y' to play Blackjack: ") == "y":
  clear()
  start_game()
