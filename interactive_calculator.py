def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
cont = "n"
while cont=="n":
  cont = "y"
  a = int(input("What's the 1st number: "))
  while cont=="y":
    print("+\n-\n*\n/")
    oper = {
      "+": add,
      "-": sub,
      "*": mul,
      "/": div,
    }
    op = input("Pick an op: ")
    b = int(input("What's the 2nd number: "))
    res = oper[op](a, b)
    print(f"{a} {op} {b} = {res}")
    cont = input("Type y to continue with res, n to start afresh: ")
    a = res
