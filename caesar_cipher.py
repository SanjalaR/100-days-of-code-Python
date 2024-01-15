alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  ans=""
  for i in text:
    if i in alphabet:
      if direction=="encode":
        num = alphabet.index(i)+shift
      elif direction=="decode":
        num = alphabet.index(i)-shift
      i=alphabet[num]
    ans+=i
  print(ans)

inp = "yes"
while(inp=="yes"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))
  shift = shift%26
  caesar(text, shift, direction)
  inp = input("Type 'yes' if you want to continue: ")
