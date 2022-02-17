from tkinter import *

FONT = ("Courier", 20, "normal")
PURPLE = "#655d8a"
BLUE = "#7897AB"
PINK = "#D885A3"
PEACH = "#FDCEB9"

# -----Countdown work------#
# ------GUI--------#
window = Tk()
window.config(padx=20, pady=20, height=400, width=400, bg=PURPLE)
window.title("Lily's Pomodorro🍅")

canvas = Canvas(width=210, height=230, bg=PURPLE, highlightthickness=0)
img_tomato = PhotoImage(file="tomato.png")
canvas.create_image(105,112, image=img_tomato)
canvas.grid(column=1, row=1)

# buttons
btn_start = Button(text="Start", font=FONT, fg=BLUE)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", font=FONT, fg=BLUE)
btn_reset.grid(column=2, row=2)

# Labels
lbl_timer = Label(text="Timer", fg=PINK, font=("Courier", 50, "bold"), bg=PURPLE)
lbl_timer.grid(column=1, row=0)

lbl_ticks = Label(text="🦄", bg=PURPLE)
lbl_ticks.grid(column=1, row=3, columnspan=2)

window.mainloop()
