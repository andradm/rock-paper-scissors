import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("ROCK, PAPER, SCISSORS\n")

""" ASCII images turned into a list for later retrieval"""
game_images = [rock, paper, scissors]

""" Player is asked which option they want"""
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

""" Computer randomly chooses its option through random module"""
computer_choice = random.randint(0,2)

"""Code is only executed if player chooses options between 0 and 2"""
if player_choice >= 0 and player_choice <= 2:
  print(game_images[player_choice])
  print("Computer chose:\n")
  print(game_images[computer_choice])

  """Options are given a variable name"""
  rock1 = 0
  paper1 = 1
  scissors1 = 2

  """If both the computer and the player choose the same option, print the following statement"""
  if computer_choice == player_choice:
    print("It's a draw.")
 # Otherwise, see who wins the game based on the following rules: rock beats scissors,
#    scissors beat paper, paper beats rock
  elif computer_choice != player_choice:
    if computer_choice == rock1 and player_choice == scissors1:
      print("You lose")
    elif computer_choice == scissors1 and player_choice == paper1:
      print("You lose")
    elif computer_choice == paper1 and player_choice == rock1:
      print("You lose")
else:
  print("You typed an invalid number. You lose!")
