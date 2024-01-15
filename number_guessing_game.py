'''
This is a number guessing game. 
The computer chooses a random number between 1 and 100 and asks the player to guess which number it chose. 
According to the player's guess, it prompts whether the guess is higher or lower than the original number. 
The game ends if the player guesses right, or if they have no attempts left.
'''
import random
print("Welcome to number guessing game!")
comp = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")
type = input("Choose a difficulty. Type 'easy' or 'hard': ")
if type=="easy":
    no = 10
elif type=="hard":
    no=5
else:
    print("Invalid!")
def game(no):
    '''Guessing game'''
    print(f"You have {no} guesses left.")
    if no<=0:
        print(f"The number was {comp}")
        return
    guess=int(input("Make a guess: "))
    def check(no):
        if guess==comp:
            print("You guessed right!")
            return 
        elif guess>comp:
            no-=1
            print("Too high")
            game(no)
        else:
            no-=1
            print("Too Low")
            game(no)
    check(no)
game(no)

