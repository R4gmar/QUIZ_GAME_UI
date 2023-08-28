THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(
        150,
        125,
        width=280,
        fill=THEME_COLOR,
        text="Some question text",
        font=("Arial", 20, "italic",))
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.score = Label(text="Score: 0", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, pady=50)

        cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=cross_image, highlightthickness=0, command=self.cross_pressed)
        self.cross.grid(column=1, row=2, pady=50)

        check_mark_image = PhotoImage(file="images/true.png")
        self.check_mark = Button(image=check_mark_image, highlightthickness=0, command=self.check_mar_pressed)
        self.check_mark.grid(column=0, row=2, pady=50,)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz")
            self.check_mark.config(state="disabled")
            self.cross.config(state="disabled")

    def check_mar_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def cross_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




