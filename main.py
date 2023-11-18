BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "images\card_front.png"
from tkinter import *

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width = 800, height=526, bg = BACKGROUND_COLOR , highlightthickness=0)

card_front_img = PhotoImage(file = CARD_FRONT)
canvas.create_image(400, 263, image = card_front_img)
canvas.grid(row = 0, column = 0, columnspan=2)
window.mainloop()