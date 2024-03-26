from tkinter import *


class ChoseCategory:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("510x380")
        self.window.title("Quiz Game")
        self.image = PhotoImage(file="E:/pyh/quiz game/images.png")
        self.window.iconphoto(False, self.image)
        self.window.config(padx=33, pady=20, bg="white")
        self.canvas = Canvas(width=180, height=200, highlightthickness=0)
        self.canvas.create_image(100, 110, image=self.image)
        self.canvas.grid(column=1, row=0)
        self.options_list = ["GeneralKnowledge", "Science", "History"]
        self.value_inside = StringVar(self.window)
        self.value_inside.set("Select an category")
        self.question_menu = OptionMenu(self.window, self.value_inside, *self.options_list)
        self.question_menu.grid(column=2, row=3, sticky="W")
        self.number_label = Label(text="Number of question", bg="white", font=("Helvetica", 10, "bold"))
        self.number_label.grid(column=0, row=3)
        self.number_entry = Entry(width=10)
        self.number_entry.grid(column=1, row=3)
        self.number = None
        self.category = None
        self.start_button = Button(self.window, text='Start Quiz', command=self.selected_item, width=20, height=2,
                                   borderwidth=0, highlightthickness=0)
        self.start_button.grid(column=1, row=4, pady=18)

        self.window.mainloop()

    def return_category(self):
        return self.category

    def return_number_of_question(self):
        return self.number

    def selected_item(self):
        self.category = format(self.value_inside.get())
        self.number = int(self.number_entry.get())
        self.window.destroy()
