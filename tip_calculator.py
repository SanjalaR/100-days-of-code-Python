print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip = int(input("What percent tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = (tip/100)+1
pay = (bill/people)*tip
print("%.2f"%pay)
