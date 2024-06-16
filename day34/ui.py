from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.lab = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.lab.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.qs = self.canvas.create_text(
            150,
            125,
            text=self.quiz.next_question(),
            fill=THEME_COLOR,
            font=FONT,
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")

        self.but1 = Button(image=true, highlightthickness=0, command=self.click_true)
        self.but1.grid(column=0, row=2)

        self.but2 = Button(image=false, highlightthickness=0, command=self.click_false)
        self.but2.grid(column=1, row=2)

        self.window.mainloop()

    def get_qs(self):
        self.canvas.config(bg='white')
        self.lab.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            qs = self.quiz.next_question()
            self.canvas.itemconfig(self.qs, text=qs)
        else:
            self.canvas.itemconfig(self.qs, text='End of quiz!')
            self.but1.config(state='disabled')
            self.but2.config(state='disabled')

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_qs)

