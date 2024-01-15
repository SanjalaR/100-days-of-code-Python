
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

rps=[rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_choice = (rps[user])
print(user_choice)
print("Computer chose: ")
comp_choice = rps[random.randint(0,2)]
print(comp_choice)
if user<0 or user>=3:
    print("You lose!")
elif user_choice==rock and comp_choice==paper:
    print("You Lose!")
elif user_choice==rock and comp_choice==scissors:
    print("You win")
elif user_choice==paper and comp_choice==rock:
    print("You win!")
elif user_choice==paper and comp_choice==scissors:
    print("You lose")
elif user_choice==scissors and comp_choice==rock:
    print("You lose")
elif user_choice==scissors and comp_choice==paper:
    print("You win")
else:
    print("Its a Draw!")
