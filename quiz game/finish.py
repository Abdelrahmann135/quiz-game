from tkinter import *


class Finish:
    def __init__(self, dic, score):
        self.window = Tk()
        self.image = PhotoImage(file="E:/pyh/quiz game/images.png")
        self.window.geometry("700x600")
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg="white")
        self.window.iconphoto(False, self.image)
        self.dic = dic
        self.score = score
        self.result()
        self.window.mainloop()

    def result(self):
        score_label = Label(text=f"Your score : {self.score}", font=("Helvetica", 18, "bold"), bg="white")
        score_label.grid(column=0, row=0, sticky="W", padx=15, pady=5)
        for i in self.dic:
            label = Message(text=f"The question : {i}\n"
                                 f"The answer : {self.dic[i]}", width=600, bg="white", font=("Helvetica", 10, "bold"))
            label.grid(sticky="W", pady=3)
