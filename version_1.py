
import tkinter as tk
from tkinter import messagebox
import random

class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Game")
        self.root.configure(bg='lightyellow')  # Set background color of the main window

        self.difficulty = tk.StringVar(value='easy')  # Default difficulty
        self.score = 0
        self.question_number = 0
        self.max_questions = 15  # Limit the number of questions

        # Create frames
        self.start_frame = tk.Frame(self.root, bg='lightyellow')
        self.quiz_frame = tk.Frame(self.root, bg='lightyellow')

        # Create widgets for start frame
        self.create_start_widgets()
        
        # Create widgets for quiz frame
        self.create_quiz_widgets()

        # Pack start frame
        self.start_frame.pack(padx=20, pady=20)

    def create_start_widgets(self):
        tk.Label(self.start_frame, text="Select Difficulty:", font=("Arial", 16), bg='lightyellow').pack(pady=10)

        difficulty_frame = tk.Frame(self.start_frame, bg='lightyellow')
        difficulty_frame.pack(pady=10)

        tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty, value='easy', font=("Arial", 14), bg='lightyellow').pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty, value='medium', font=("Arial", 14), bg='lightyellow').pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty, value='hard', font=("Arial", 14), bg='lightyellow').pack(side=tk.LEFT)

        self.start_button = tk.Button(self.start_frame, text="Start Quiz", command=self.start_quiz, font=("Arial", 16), bg='yellow', fg='black')
        self.start_button.pack(pady=20)

    def create_quiz_widgets(self):
        tk.Label(self.quiz_frame, text="Math Quiz", font=("Arial", 20), bg='lightyellow').pack(pady=10)

        self.question_label = tk.Label(self.quiz_frame, text="Select difficulty to start", font=("Arial", 16), bg='lightyellow')
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit Answer", command=self.check_answer, font=("Arial", 16), bg='yellow', fg='black')
        self.submit_button.pack(pady=20)

        self.score_label = tk.Label(self.quiz_frame, text=f"Score: {self.score}", font=("Arial", 16), bg='lightyellow')
        self.score_label.pack(pady=10)

        self.restart_button = tk.Button(self.quiz_frame, text="Restart Quiz", command=self.restart_quiz, font=("Arial", 16), bg='yellow', fg='black')
        self.restart_button.pack(pady=20)
        self.restart_button.pack_forget()  # Hide restart button initially

    def get_range_and_operations(self):
        level = self.difficulty.get()
        if level == 'easy':
            return (1, 10), ['+', '-']
        elif level == 'medium':
            return (1, 50), ['+', '-', '*']
        elif level == 'hard':
            return (1, 100), ['+', '-', '*', '/']

    def start_quiz(self):
        # Hide start frame and show quiz frame
        self.start_frame.pack_forget()
        self.quiz_frame.pack(padx=20, pady=20)
        self.reset_quiz()

    def reset_quiz(self):
        self.score = 0
        self.question_number = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

    def next_question(self):
        if self.question_number >= self.max_questions:
            self.end_quiz()
            return
        
        number_range, operations = self.get_range_and_operations()
        self.num1 = random.randint(*number_range)
        self.num2 = random.randint(*number_range)
        self.operation = random.choice(operations)

        if self.operation == '/':
            while self.num2 == 0:
                self.num2 = random.randint(*number_range)
            self.num1 = self.num1 * self.num2  # Ensure divisibility
            self.correct_answer = self.num1 // self.num2
        elif self.operation == '+':
            self.correct_answer = self.num1 + self.num2
        elif self.operation == '-':
            self.correct_answer = self.num1 - self.num2
        elif self.operation == '*':
            self.correct_answer = self.num1 * self.num2

        self.question_label.config(text=f"What is {self.num1} {self.operation} {self.num2}?")
        self.answer_entry.delete(0, tk.END)  # Clear the entry field

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.score += 1
                messagebox.showinfo("Correct!", "That's the correct answer!")
            else:
                messagebox.showinfo("Incorrect", f"Oops! The correct answer was {self.correct_answer}.")
            
            self.question_number += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.next_question()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"Quiz completed! Your final score is {self.score}.")
        self.restart_button.pack(pady=20)

    def restart_quiz(self):
        # Hide quiz frame and show start frame
        self.quiz_frame.pack_forget()
        self.start_frame.pack(padx=20, pady=20)

# Create the main window
root = tk.Tk()
game = MathQuiz(root)
root.mainloop()
