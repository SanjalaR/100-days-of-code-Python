'''
This is a simple version of BlackJack.
The dealer (computer) deals 2 cards each to the player and itself. 
The objective is to make the total reach as close to 21 without going over. 
Having a straight 21 is called a Blackjack.
In each step, the player can either ask another card or stand.
'''

import random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print("Welcome to Blackjack!\n")
play = 'y'
user = []
user.append(random.choice(card))
score = user[0]
i = 1
comp = []
comp.append(random.choice(card))
comp.append(random.choice(card))
csc = comp[0]+ comp[1]

def lose(score, csc):
    print(f"Your score: {score}, Comp score: {csc}\n")
    print("You went over. You lose!")

def check(user, score, comp, csc):
    if csc==21:
        print(f"Your final cards: {user}, your final score: {score}\n")
        print(f"Comp's final cards: {comp}, Comp's final score: {csc}")
        print("Computer wins!")
        return False
    elif csc>21:
        print(f"Your score: {score}, Comp score: {csc}\n")
        print("Computer loses, you win!")
        return False
    elif score>21:
        lose(score, csc)
        return False
    elif score==21:
        print(f"Your final cards: {user}, your final score: {score}")
        print(f"Comp's final cards: {comp}, Comp's final score: {csc}")
        print("You win!")
        return False
    else:
        return True
cont = True

while(play=='y'):
    user.append(random.choice(card))
    score+=user[i]
    i+=1
    print(f"Your cards: {user}, current score: {score}")
    print(f"Computer's first card: {comp[0]}")
    cont = check(user, score, comp, csc)
    if (not cont):
        break
    play = input("Type 'y' to hit, 'n' to pass: ")

if play=='n':
    while csc<16:
        comp.append(random.choice(card))
        csc+=comp[len(comp)-1]
    print(f"Your final cards: {user}, your final score: {score}")
    print(f"Comp's final cards: {comp}, Comp's final score: {csc}")
    cont = check(user, score, comp, csc)
    if cont:
        if csc<score:
            print("You win!")
        elif csc>score:
            print("Comp wins!")
        else:
            print("It is a draw")
