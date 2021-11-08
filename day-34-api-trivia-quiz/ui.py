import tkinter
from quiz_brain import QuizBrain
from time import sleep

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizlerr..")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(0, 50))

        self.question_text = self.canvas.create_text(150, 125, width=280, text="text", fill=THEME_COLOR)
        self.canvas.itemconfig(self.question_text, font=("Arial", 18, "italic"))

        self.true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=self.true_image,
                                          highlightthickness=0,
                                          command=self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=(25, 25), pady=(25, 25))

        self.false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=self.false_image,
                                           highlightthickness=0,
                                           command=self.false_pressed)
        self.false_button.grid(column=1, row=2, padx=(25, 25), pady=(25, 25))

        self.score_label = tkinter.Label(text=f"Score: {self.quiz.score}",
                                         bg=THEME_COLOR,
                                         fg="white",
                                         font=("Arial", 20, "normal"))
        self.score_label.grid(column=1, row=0, pady=(0, 5))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Sorry, you have finished all the questions.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)

