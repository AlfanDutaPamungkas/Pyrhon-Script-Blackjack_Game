from art import logo
import random
import os

operation_system = os.name

def start():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
  if 11 in card and sum(card) > 21:
      card.remove(11)
      card.append(1)
  return sum(card)

def compare(user,com):
  if user == 21:
    return "You win"
  elif user == com:
    return "it's a daw"
  elif com == 0:
    return "You lose opponent has a BlackJack"
  elif user == 0:
    return "You win ith BlackJack"
  elif user > 21:
    return "You lose"
  elif com > 21:
    return "You win"
  elif user > com:
    return "You win"
  else:
    return "You lose"

def black_jack():
  user_card = []
  com_card = []
  is_over = False
  
  match operation_system:
    case "posix":os.system("clear")
    case "nt":os.system("cls")
  
  print(logo)
  for _ in (0,2):
    user_card.append(start())
    com_card.append(start())
  
  while not is_over:
    user_amount = calculate_score(user_card)
    com_amount = calculate_score(com_card)
  
    print(f"Your cards : {user_card}, current score : {user_amount}")
    print(f"Computer's first card : {com_card[0]}")
    
    if user_amount == 0 or com_amount == 0 or user_amount >= 21:
      is_over = True
    else:
      user_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_decision == "y":
        user_card.append(start())
      else:
        is_over = True
  
  while com_amount != 0 and com_amount < 17:
    com_card.append(start())
    com_amount = calculate_score(com_card)
    
  print(f"Your final hand : {user_card}, final score : {user_amount}")
  print(f"Computer final hand : {com_card}, final score : {com_amount}")
  
  print(compare(user_amount, com_amount))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y" :
  black_jack()