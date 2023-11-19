from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\card_front.png"
CARD_BACK = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\card_back.png"
WRONG_BTN_IMAGE = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\wrong.png"
RIGHT_BTN_IMAGE = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\\right.png"
DATA_FILE = "D:\Coding\Python\Angela\Projects\\flash-card-project\data\\french_words.csv"
WORDS_TO_LEARN = "D:\Coding\Python\Angela\Projects\\flash-card-project\data\\words_to_learn.csv"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
try:
    word_data_frame = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    word_data_frame = pandas.read_csv(DATA_FILE)
except pandas.errors.EmptyDataError:
    word_data_frame = pandas.read_csv(DATA_FILE)


word_dict = word_data_frame.to_dict(orient="records")
chosen_word={}


def next_card():
    global chosen_word
    global flip_timer
    window.after_cancel(flip_timer)
    chosen_word = choice(word_dict)
    french_word = chosen_word['French']
    canvas.itemconfigure(card_title, text="French", fill='black')
    canvas.itemconfigure(card_word, text=french_word, fill='black')
    canvas.itemconfigure(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_to_back)
def flip_to_back():
    english_word = chosen_word["English"]
    canvas.itemconfigure(card_title, text="English", fill='white')
    canvas.itemconfigure(card_word, text=english_word, fill='white')
    canvas.itemconfigure(canvas_image, image=card_back_img)

def update_word_list():
    if len(word_dict)!=0:
        next_card()
        word_dict.remove(chosen_word)
        df = pandas.DataFrame.from_records(word_dict)
        df.to_csv(WORDS_TO_LEARN, index=False)
    else:
        return

card_front_img = PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong_image = PhotoImage(file=WRONG_BTN_IMAGE)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file=RIGHT_BTN_IMAGE)
right_button = Button(image=right_image, highlightthickness=0, command=update_word_list)
right_button.grid(row=1, column=1)
flip_timer = window.after(3000, flip_to_back)
next_card()

window.mainloop()
