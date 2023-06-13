from tkinter import *


window = Tk()
window.title("Calculator")
window.resizable(False, False)
def press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:

        total = str(eval(equation_text))
        equation_label.set(total)
        clear()
    except SyntaxError:
        equation_label.set('syntax error')
        clear()
    except ZeroDivisionError:
        equation_label.set('arithmetic error')
        clear()


def clear():
    global equation_text

    equation_text = ''
    # equation_label.set('0')


equation_text = ''
equation_label = StringVar()
label = Label(window, text='F', textvariable=equation_label,
              font=('Arial', 20),
              bg='white',
              width=20,
              height=2)
label.pack()
frame = Frame(window)
frame.pack()

button_width = 9
Button(frame, text="1", command=lambda: press(1), width=button_width, height=4).grid(row=0, column=0)

Button(frame, text="2", command=lambda: press(2), width=button_width, height=4).grid(row=0, column=1)
Button(frame, text="3", command=lambda: press(3), width=button_width, height=4).grid(row=0, column=2)
Button(frame, text="4", command=lambda: press(4), width=button_width, height=4).grid(row=1, column=0)
Button(frame, text="5", command=lambda: press(5), width=button_width, height=4).grid(row=1, column=1)
Button(frame, text="6", command=lambda: press(6), width=button_width, height=4).grid(row=1, column=2)
Button(frame, text="7", command=lambda: press(7), width=button_width, height=4).grid(row=2, column=0)
Button(frame, text="8", command=lambda: press(8), width=button_width, height=4).grid(row=2, column=1)
Button(frame, text="9", command=lambda: press(9), width=button_width, height=4).grid(row=2, column=2)
Button(frame, text="0", command=lambda: press(0), width=button_width, height=4).grid(row=3, column=1)

Button(frame, text="+", command=lambda: press('+'), width=button_width, height=4).grid(row=0, column=3)
Button(frame, text="-", command=lambda: press('-'), width=button_width, height=4).grid(row=1, column=3)
Button(frame, text="/", command=lambda: press('/'), width=button_width, height=4).grid(row=2, column=3)
Button(frame, text="*", command=lambda: press('*'), width=button_width, height=4).grid(row=3, column=3)
Button(frame, text=".", command=lambda: press('.'), width=button_width, height=4).grid(row=3, column=0)

Button(frame, text="=", command=equals, width=button_width, height=4).grid(row=3, column=2)


Button(window, text="clr", command=clear, width=window.winfo_depth(), height=4).pack()


window.mainloop()
