from tkinter import *
import time


WIDTH = 500
HEIGHT = 500
window = Tk()


# window.geometry(f'{WIDTH}x{HEIGHT}')
window.title('Clock')
window.config(bg='black')


def update_time():
    time_string = time.strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    day_string = time.strftime('%A')
    day_label.config(text=day_string)

    date_string = time.strftime('%B %d, %Y')
    date_label.config(text=date_string)

    window.after(1000, update_time)


time_label = Label(window, font=('Arial', 50), fg='green', bg='black')
time_label.pack()

day_label = Label(window, font=('Ink Free', 50), fg='green', bg='black')
day_label.pack()

date_label = Label(window, font=('Times New Roman', 50), fg='green', bg='black')
date_label.pack()

update_time()

window.mainloop()
