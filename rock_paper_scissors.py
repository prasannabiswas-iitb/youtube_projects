#### Rock Paper Scissors

print("Paper v/s rock: paper wins")
print("Paper v/s scissors: scissors wins")
print("Rock v/s scissors: rock wins")

asc_wins = 0
computer_wins = 0

import random
for i in range(5):
  asc_choice = input("Choose rock, paper or scissors: ")
  possible_actions = ["rock", "paper", "scissors"]

  computer_choice = random.choice(possible_actions)

  print(f"\nASC students chose {asc_choice}, computer chose {computer_choice}.\n")

  if asc_choice == computer_choice:
    print("It's a tie!")
  elif asc_choice == "paper":
    if computer_choice == "rock":
      print("Paper wins!")
      asc_wins += 1
    else:
      print("Scissors win!")
      computer_wins += 1
  elif asc_choice == "rock":
    if computer_choice == "scissors":
      print("Rock wins!")
      asc_wins += 1
    else:
      print("Paper wins!")
      computer_wins += 1
  elif asc_choice == "scissors":
    if computer_choice == "paper":
      print("Scissors win!")
      asc_wins += 1
    else:
      print("Rock wins!")
      computer_wins += 1
  else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
    i -= 1
  print("=========================================================")

if asc_wins > computer_wins:
  print("ASC students won the game!")
elif asc_wins < computer_wins:
  print("Computer won the game!")
else:
  print("It's a tie!")