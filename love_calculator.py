print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
name = name1 + name2
name = name.lower()
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
true = t+r+u+e
l=name.count('l')
o=name.count('o')
v=name.count('v')
love = l+o+v+e
score = int(str(true)+str(love))
if(10>score or score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
