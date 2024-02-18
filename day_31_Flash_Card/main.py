from tkinter import *
import random
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
word = {}
to_learn = {}

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def show_english_word():
    english_word = word["English"]
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    french_word = word["French"]
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    flip_timer = window.after(3000, show_english_word)

def is_known():
    to_learn.remove(word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
check_button.grid(column=1, row=1)  # Position the button in the grid

x_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
x_button.grid(column=0, row=1)  # Position the button in the grid

flip_timer = window.after(3000, show_english_word)
next_card()

window.mainloop()
