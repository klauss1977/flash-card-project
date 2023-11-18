BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\card_front.png"
WRONG_BTN_IMAGE = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\wrong.png"
RIGHT_BTN_IMAGE = "D:\Coding\Python\Angela\Projects\\flash-card-project\images\\right.png"
from tkinter import *

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width = 800, height=526, bg = BACKGROUND_COLOR , highlightthickness=0)

card_front_img = PhotoImage(file = CARD_FRONT)
canvas.create_image(400, 263, image = card_front_img)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Mot", font=("Arial", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan=2)
wrong_image = PhotoImage(file = WRONG_BTN_IMAGE)
wrong_button = Button(image = wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file = RIGHT_BTN_IMAGE)
right_button = Button(image = right_image, highlightthickness=0)
right_button.grid(row=1, column=1)
window.mainloop()