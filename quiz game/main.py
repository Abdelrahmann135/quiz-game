from tkinter import messagebox

from chose_category import ChoseCategory
from start_quiz import StartQuiz
cancel = True
while cancel:
    chose_category_page = ChoseCategory()
    category = chose_category_page.return_category()
    number = chose_category_page.return_number_of_question()
    if number <= 0 or number > 10:
        cancel = messagebox.askokcancel("Error", "Number of question should be in range of 0 to 10")
    elif category == "Select an category":
        cancel = messagebox.askokcancel("Error", "Please choose category")
    else:
        start_quiz = StartQuiz(category, number)
        break
