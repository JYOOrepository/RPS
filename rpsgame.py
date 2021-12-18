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

import random

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

computer_choice = [rock, paper, scissors]

random = random.choice(computer_choice)

if user_choice >= 3:
  print('You typed an invalid number, you lose!')
elif user_choice == 0 and random == rock:
  print("Computer chose:\n" + random)
  print('It\'s a tie.')
elif user_choice == 1 and random == rock:
  print("Computer chose:\n" + random)
  print('You Win')
elif user_choice == 2 and random == rock:
  print("Computer chose:\n" + random)
  print('You Lose')
elif user_choice == 0 and random == paper:
  print("Computer chose:\n" + random)
  print('You Lose')
elif user_choice == 1 and random == paper:
  print("Computer chose:\n" + random)
  print('It\'s a tie.')
elif user_choice == 2 and random == paper:
  print("Computer chose:\n" + random)
  print('You Win')
elif user_choice == 0 and random == scissors:
  print("Computer chose:\n" + random)
  print('You Win')
elif user_choice == 1 and random == scissors:
  print("Computer chose:\n" + random)
  print('You Lose')
elif user_choice == 2 and random == scissors:
  print("Computer chose:\n" + random)
  print('It\'s a tie.')
