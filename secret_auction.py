dict={}
cont = "y"
def clear() -> None:
    print("\033[H\033[2J", end="", flush=True)
while cont=="y":
    clear()
    print("Welcome to the secret auction program. ")
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    dict[name] = bid
    cont = input("If there are any other bidders, type y: ")
highest = 0
high_name = ""
for key in dict:
    if dict[key]>highest:
        highest = dict[key]
        high_name = key
clear()
print(f"Winner if {high_name} with a bid of ${highest}")
