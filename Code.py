import tkinter as tk
from tkinter import messagebox

# Quiz data: Questions, options, correct answers, and explanations
quiz_data = [
    {
        "question": "Who is the current President of the United States?",
        "options": ["Joe Biden", "Donald Trump", "Barack Obama", "George W. Bush"],
        "answer": "Joe Biden",
        "explanation": "Joe Biden is the current President, having taken office in January 2021."
    },
    {
        "question": "How many amendments does the U.S. Constitution have?",
        "options": ["27", "25", "30", "33"],
        "answer": "27",
        "explanation": "The U.S. Constitution has 27 amendments. The first 10, known as the Bill of Rights, were ratified in 1791."
    },
    {
        "question": "Which branch of government is responsible for making federal laws?",
        "options": ["Executive", "Judicial", "Legislative", "None of the above"],
        "answer": "Legislative",
        "explanation": "The Legislative branch, consisting of the House of Representatives and the Senate, makes federal laws."
    }
]

current_question = 0

def submit_answer():
    global current_question
    selected_option = var.get()
    if selected_option == quiz_data[current_question]['answer']:
        messagebox.showinfo("Correct!", "That's right!\n" + quiz_data[current_question]['explanation'])
    else:
        messagebox.showinfo("Incorrect!", "Actually, it's incorrect.\n" + quiz_data[current_question]['explanation'])
    
    current_question += 1
    if current_question < len(quiz_data):
        load_question(current_question)
    else:
        messagebox.showinfo("End of Quiz", "You've completed the quiz!")
        root.destroy()

def load_question(index):
    var.set(None)  # Clear previous selection
    question_label.config(text=quiz_data[index]['question'])
    for i, option in enumerate(quiz_data[index]['options']):
        radio_buttons[i].config(text=option, value=option)

# Set up the main window
root = tk.Tk()
root.title("U.S. Government and Politics Quiz")

# Question label
question_label = tk.Label(root, font=('Arial', 14), wraplength=400)
question_label.pack(pady=20)

# Radio button for options
var = tk.StringVar(value="None")
radio_buttons = [
    tk.Radiobutton(root, text="", variable=var, value=None, font=('Arial', 12))
    for _ in range(4)
]
for rb in radio_buttons:
    rb.pack(anchor="w")

# Button to submit answer
submit_button = tk.Button(root, text="Submit Answer", command=submit_answer)
submit_button.pack(pady=20)

# Load the first question
load_question(current_question)

# Start the GUI
root.mainloop()
