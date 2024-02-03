# Using file handling to write multiple letters
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        new_name = name.strip()
        new_letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as files:
            files.write(new_letter)


