question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to "
             "eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "text": "The HTML5 standard was published in 2014.",
        "answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "text": "The first computer bug was formed by faulty wires.",
        "answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "text": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "text": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        "answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "text": "Linus Torvalds created Linux and Git.",
        "answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "text": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "text": "AMD created the first consumer 64-bit processor.",
        "answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "text": "'HTML' stands for Hypertext Markup Language.",
        "answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "text": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "text": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "answer": "False",
        "incorrect_answers": [
            "True"
        ]
    }
]


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for i in question_data:
    q = Question(i["text"], i["answer"])
    question_bank.append(q)


class QuizBrain:
    def __init__(self, qlist):
        self.qlist = qlist
        self.qno = 0
        self.score = 0

    def next_ques(self):
        ans = input(f"Q.{self.qno + 1}. {self.qlist[self.qno].text} (True/False)?: ")
        if ans == self.qlist[self.qno].answer:
            self.score += 1
            self.qno += 1
            print(f"You got it right!\nYour score is {self.score}")
            if self.qno < len(self.qlist):
                self.next_ques()
            else:
                print(f"The quiz is done!\nYour final score is {self.score}")

        else:
            print(f"You are wrong!\nYour score is {self.score}")
            self.qno += 1
            if self.qno < len(self.qlist):
                self.next_ques()


start = QuizBrain(question_bank)
start.next_ques()
