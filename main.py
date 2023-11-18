from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\card_front.png"
WRONG_BTN_IMAGE = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\wrong.png"
RIGHT_BTN_IMAGE = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\\right.png"
DATA_FILE = "D:\Coding\Python\Angela\Projects\\flash-card-project\data\\french_words.csv"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
word_data_frame = pandas.read_csv(DATA_FILE)
word_dict = word_data_frame.to_dict(orient="records")


def next_card():
    new_french_word = choice(word_dict)['French']
    canvas.itemconfigure(card_title, text="French")
    canvas.itemconfigure(card_word, text=new_french_word)


card_front_img = PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong_image = PhotoImage(file=WRONG_BTN_IMAGE)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file=RIGHT_BTN_IMAGE)
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
next_card()
window.mainloop()
