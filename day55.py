from flask import Flask
import random

# $env:FLASK_APP='day55.py'
app = Flask(__name__)
NUMBER = random.randint(0, 9)


@app.route('/')
def start_page():
    return ('<h1 style="color: #000080"> Guess a number between 0 and 9 </h1>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDdtYW5jdWRpc3ducHF6eWQ0OXBlcHV5ZXpzaHp2dG5tN2dmNXdmMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4JVTF9zR9BicshFAb7/giphy.gif" width=400px height=400px>')


@app.route('/<int:guess>')
def guessed(guess):
    if guess < NUMBER:
        return ('<h1 style="color: red"> Too low, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGJ6NHV5YjhvNGZhdDR6ZXZqOGN0eXRrN20wazZwZjBlODM1NngwMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKHWfu68Q6XOz2I6Y/giphy.gif" width=400px height=400px')
    elif guess > NUMBER:
        return ('<h1 style="color: green"> Too high, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTI3aGhodWliOWRneHhsZzluZ3JvN2VveGN1OXlzemZ5bGtrcTUzaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IhlTq8YYTgKZDD6XPk/giphy.gif" width=400px height=400px')
    else:
        return ('<h1 style="color: #000080"> You found it! </h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3BydjZycnlnbDRkN3pndHc5NWw3MjFjdnptNnJpZmZkeWd4endlayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YTbZzCkRQCEJa/giphy.gif" height=400px width=400px')


if __name__ == '__main__':
    app.run(debug=True)
