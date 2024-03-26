from tkinter import *
from Data import *
from random import *
from finish import Finish


class StartQuiz:
    def __init__(self, category, number):
        self.window = Tk()
        self.image = PhotoImage(file="E:/pyh/quiz game/images.png")
        self.window.geometry("650x380")
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=10, bg="white")
        self.window.iconphoto(False, self.image)
        self.number = number
        self.score = 0
        self.question_label = Message(font=("Helvetica", 11, "bold"), bg="white", width=530)
        self.label = Label(font=("Helvetica", 20, "bold"), bg="white", padx=3, pady=15)
        self.label.grid(column=0, row=1, columnspan=2, sticky="W")
        self.question_label.grid(column=0, row=3, columnspan=2, sticky="W", pady=15)
        self.questions = categories[category].copy()
        self.question_correct_answer = {}
        self.number_of_question = 1
        self.next_question()
        self.window.mainloop()

    def finish(self):
        self.window.destroy()
        Finish(self.question_correct_answer, self.score)

    def next_question(self):
        if self.number_of_question <= self.number:
            self.ask_question()
            self.number_of_question += 1

    def ask_question(self):
        question = choice(self.questions)

        def check_answer():
            user_answer = var.get()
            answer = question["correct_answer"]
            if user_answer == answer:
                self.score += 1
            else:
                self.question_correct_answer[f"{self.number_of_question - 1} : {question["question"]}"] = answer
            if self.number_of_question <= self.number:
                self.next_question()
                for n in radio_list:
                    n.destroy()
            else:
                self.finish()
        choices_list = question["incorrect_answers"]
        choices_list.append(question["correct_answer"])
        shuffle(choices_list)
        self.label.config(text=f"Question {self.number_of_question}")
        self.question_label.config(text=f"{question["question"]}")

        var = StringVar(value=" ")
        radio_list = []
        for i in range(4):
            c = Radiobutton(self.window, text=choices_list[i],
                            variable=var, value=choices_list[i], font=("Helvetica", 10, "bold"), bg="white")
            radio_list.append(c)
            radio_list[i].grid(column=0, row=i+4, sticky="W", pady=2)

        button = Button(text="Next", command=check_answer, borderwidth=0, highlightthickness=0, width=10, height=2)
        button.grid(column=2, row=8)
        if self.number_of_question == self.number:
            button.config(text="Finish")

        self.questions.remove(question)
