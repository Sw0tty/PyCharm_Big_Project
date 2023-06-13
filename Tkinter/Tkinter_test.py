from tkinter import *
from tkinter import messagebox  # submodule of tkinter
from tkinter import colorchooser  # submodule of tkinter
from tkinter import filedialog  # submodule of tkinter
from tkinter import ttk  # submodule of tkinter
import time


# widgets = GUI element: buttons, textboxes, images, radiobuttons
# windows = server as a container to hold or contain there widgets

# --- window ---

WIDTH = 1000
HEIGHT = 500

window = Tk()  # creating an instance of a window
window.geometry(f'{WIDTH}x{HEIGHT}')  # size of window
window.title('First GUI program')

icon = PhotoImage(file=r'D:\PyProjects\PyCharm_Big_Project\PyFiles\img\test_img.png')  # path to photo
window.iconphoto(True, icon)  # set icon photo
window.config(background='#bdd8f0')  # set settings for window
# ---------------------------


# --- label ---
# label = an area widget that holds text and/or image

photo = PhotoImage(file=r'D:\PyProjects\PyCharm_Big_Project\PyFiles\img\pc_logo.png')

label = Label(window,
              text="Hellow World!",         # text
              font=('Arial', 40, 'bold'),   # text font
              fg='green',                   # color text
              bg='black',                   # background label color
              relief='raised',              # style of border
              bd=10,                        # size of border
              padx=20,                      # space right and left
              pady=20,                      # space above and below
              #image=icon,                   # placing image
              compound='right')             # placement method

label.pack()                                # placing label on window
# label.place(x=100, y=100)                 # placing label on window for X and Y

# --------------------------


# --- button ---
# button = clickable area

count = 0


def click():
    global count
    count += 1
    print(f"Button click {count} times")


button = Button(window,
                text="Click me",
                font=('Comic Sans MS', 15),
                command=click,
                fg='green',
                bg='black',
                activeforeground='green',
                activebackground='black',
                state='active',
                # image=icon,
                compound='bottom')

button.pack()
# --------------------------


# --- textbox ---
# textbox = accept a single line of user input

def submit():
    username = entry.get()
    if username:
        print(f"Hello {username}")
    # entry.config(state='disabled')        # we can change config

def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


entry = Entry(window,
              font=('Times New Roman', 25),
              fg='green',
              bg='black',
              show='*')                     # hiding input characters

# entry.insert(0, 'Spongebob')              # inserting text in textbox
entry.pack(side='left')

submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack(side='left')

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side='left')

backspace = Button(window,
                   text="Backspace",
                   command=backspace)
backspace.pack(side='left')
# --------------------------


# --- check button ---
# check button = clickable area

def display():
    if x.get():
        print("You agree")
    else:
        print("You disagree")


x = IntVar()  # BoolVar, StringVar

check_button = Checkbutton(window,
                           text="I agree to something",
                           font=("Arial", 10),
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           fg='green',
                           bg='black',
                           activeforeground='green',
                           activebackground='black',
                           # image=icon,
                           padx=25,
                           pady=10)

check_button.pack()
# --------------------------


# --- radio button ---
# radio button =

def order():
    if x.get() == 0:
        print("Pizza")
    elif x.get() == 1:
        print("Hamburger")
    else:
        print("Hotdog")

food = ['pizza', 'hamburger', 'hotdog']

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],                # adds texts to radio buttons
                               font=("Arial", 15),
                               variable=x,                  # groups radio buttons together
                               value=i,
                               fg='green',
                               bg='black',
                               activeforeground='green',
                               activebackground='black',
                               command=order,
                               # image=icon,
                               padx=25,
                               pady=10)

    radio_button.pack(anchor=W)
# --------------------------


# --- scale ---
# scale =

def submit_b2():
    print(f"Temperature {scale.get()}")


scale = Scale(window,
              from_=0,
              to=100,
              length=300,
              orient=HORIZONTAL,
              font=('Consolas', 20),
              tickinterval=20,
              showvalue=True,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black'
              )


button_2 = Button(window, text="Submit", command=submit_b2)

# scale.set(50)
scale.pack(side='left')
button_2.pack(side='left')
# --------------------------


# --- listbox ---
# listbox = listing text items

def submit_b3():

    food = []

    for i in list_box.curselection():
        food.insert(i, list_box.get(i))

    print("You have order:")
    for i in food:
        print(i)

def add():
    list_box.insert(list_box.size(), entry_2.get())
    list_box.config(height=list_box.size())


def delete_2():
    for i in reversed(list_box.curselection()):
        list_box.delete(i)
    # list_box.delete(list_box.curselection())
    list_box.config(height=list_box.size())


list_box = Listbox(window,
                   font=('Constantia', 20),
                   bg='black',
                   fg='green',
                   width=12,
                   selectmode=MULTIPLE)

list_box.insert(1, 'pizza')
list_box.insert(2, 'pasta')
list_box.insert(3, 'garlic bread')
list_box.insert(4, 'soup')
list_box.insert(5, 'salad')

list_box.config(height=list_box.size())  # cutting off free space

entry_2 = Entry(window)
entry_2.pack()

add_button = Button(window, text="Add", command=add)
submit_button_2 = Button(window, text="Submit", command=submit_b3)
delete_button_2 = Button(window, text="Delete", command=delete_2)

list_box.pack()
submit_button_2.pack()
add_button.pack()
delete_button_2.pack()
# --------------------------


# --- message box ---
# message box =

def message_click():
    # messagebox.showinfo(title='This is info message box', message='Just a message about info you')
    # messagebox.showwarning(title='Warning message', message='Something wrong')
    # messagebox.showerror(title='Error message!', message='Oops!')

    # if messagebox.askokcancel(title='Ask ok cancel', message="""'You're right?"""):
    #     print('Yap!')
    # else:
    #     print('Oh no!')

    # if messagebox.askretrycancel(title='Ask ok cancel', message="""'You're right?"""):
    #     print('Yap!')
    # else:
    #     print('Oh no!')

    # if messagebox.askyesno(title='Ask Yes/no', message='Do you like cake?'):
    #     print('Im too')
    # else:
    #     print('Crap')

    # print(messagebox.askyesno(title='Ask Yes/no', message='Do you like cake?'))
    # print(messagebox.askquestion(title='Ask question', message='Do you like pie?'))

    print(messagebox.askyesnocancel(title='Y/N/C', message='Do you like to code?', icon='info'))

button_3 = Button(window, text="For message", command=message_click)

button_3.pack()
# --------------------------


# --- color chooser ---
# color chooser =
def color_click():
    color = colorchooser.askcolor()  # return tuple ((R, G, B), HEX)
    color_hex = color[1]
    print(f"You picked {color_hex}")
    window.config(bg=color_hex)


chooser_button = Button(window, text="Color choose", command=color_click)

chooser_button.pack()
# --------------------------


# --- text widget ---
# text widget = contain multiple lines of text
def submit_text_area():
    user_input = text.get(1.0, END)
    print(user_input)


text = Text(window,
            font=('Ink Free', 20),
            bg='light yellow',
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='red')

button_4 = Button(window, text="For text area", command=submit_text_area)

button_4.pack(side='left')
text.pack(side='left')
# --------------------------


# --- filedialog ---
# filedialog =
def open_file():
    filepath = filedialog.askopenfilename(initialdir=r'..\PyFiles\python_files_works\files_dir',
                                          title="Open file",
                                          filetypes=(('text files', '*.txt'), ('all files', '*')))

    with open(filepath, 'r', encoding='utf8') as file:
        content = [i.strip() for i in file.readlines()]
        print(content)


def save_file():
    file = filedialog.asksaveasfile(initialdir=r'..\PyFiles\python_files_works\files_dir',
                                    defaultextension='.txt',
                                    filetypes=[('Text file', '.txt'), ('HTML files', '.html'),
                                               ('All files', '*')])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()


button_5 = Button(window, text="Open File", command=open_file)
button_5.pack(side='left')

button_6 = Button(window, text="Save File", command=save_file)
button_6.pack(side='left')
# --------------------------


# --- menubar ---
# menubar =

menu_bar = Menu(window)

window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False, bg='black', fg='green')
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()  # separate commands Example Save | Exit
file_menu.add_command(label="Exit")

edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
# --------------------------


# --- frame ---
# frame = container to group and hold widgets
def top_b():
    print("Press W")


def left_b():
    print("Press A")


def bottom_b():
    print("Press S")


def right_b():
    print("Press D")


frame = Frame(window, bg='pink', bd=5, relief=RAISED)
frame.pack()

Button(frame, text="W", font=("Consolas", 15), width=3, command=top_b).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 15), width=3, command=left_b).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 15), width=3, command=bottom_b).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 15), width=3, command=right_b).pack(side=LEFT)
# --------------------------


# --- another windows ---
# another windows =
def create_window():
    new_window = Toplevel()


Button(window, text="Create a new window", command=create_window).pack()

frame = Frame(window, bg='pink', bd=5, relief=RAISED)
frame.pack()

# --------------------------


# --- tabs ---
# tabs =
notebook = ttk.Notebook(window)

tab_1 = Frame(notebook)  # new frame for tab 1
tab_2 = Frame(notebook)  # new frame for tab 2

notebook.add(tab_1, text="Tab 1")
notebook.add(tab_2, text="Tab 2")
notebook.pack(expand=True)  # fill='both'

Label(tab_1, text="This tab 1", width=50, height=25).pack()
Label(tab_2, text="This tab 2", width=50, height=25).pack()
# --------------------------


# --- grid ---
# grid =

# first_name_label = Label(window, text="First name: ").grid()
# first_name_entry = Entry(window).grid()
# notebook.add(first_name_label)
# notebook.add(first_name_entry)

# --------------------------


# --- progress bar ---
# progress bar =
def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+'%')
        text_process.set(str(download)+'/'+str(GB)+" completed")
        window.update_idletasks()


percent = StringVar()
text_process = StringVar()

bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200)
bar.pack(pady=10)

Label(window, textvariable=percent).pack()
Label(window, textvariable=text_process).pack()

Button(window, text="Download", command=start).pack()
# --------------------------


# --- canvas ---
# canvas = widget that is used to draw graphs, plots, images in a window

canvas = Canvas(window, height=500, width=500)
blue_line = canvas.create_line(0, 0, 500, 500, fill='blue', width=5)
red_line = canvas.create_line(0, 500, 500, 0, fill='red', width=5)
canvas.create_rectangle(50, 50, 250, 250, fill='pink')
points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill='yellow', outline='black', width=5)
canvas.create_arc(0, 0, 500, 500, fill='green', style=PIESLICE, start=270, extent=180)

# --pokeball--
canvas.create_arc(0, 0, 500, 500, fill='red', extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill='white', start=180, extent=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill='white', width=10)
# ------------

canvas.pack()

# --------------------------


# --- key events ---
# key events =
def do_something(event):
    label.config(text=event.keysym)


window.bind('<Key>', do_something)
key_label = Label(window)
key_label.pack()

# --------------------------


# --- mouse events ---
# mouse events =
def do_for_mouse(event):
    print(f"X = {event.x}, Y = {event.y}")


# window.bind('<Button-1>', do_for_mouse)  # LMB
# window.bind('<Button-2>', do_for_mouse)  # CMB
# window.bind('<Button-3>', do_for_mouse)  # RMB
# window.bind('<ButtonRelease>', do_for_mouse)  # event releasing button
# window.bind('<Leave>', do_for_mouse)  # event when mouse leave the window
# window.bind('<Motion>', do_for_mouse)  # event when mouse moved
# --------------------------


# --- drag and drop ---
# drag and drop =
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


label = Label(window, bg='red', width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg='blue', width=10, height=5)
label2.place(x=100, y=100)

label.bind('<Button-1>', drag_start)
label.bind('<B1-Motion>', drag_motion)

label2.bind('<Button-1>', drag_start)
label2.bind('<B1-Motion>', drag_motion)
# --------------------------


# --- moving polygon ---
# moving polygon =
def move_up(event):
    label_img.place(x=label_img.winfo_x(), y=label_img.winfo_y()-10)


def move_down(event):
    label_img.place(x=label_img.winfo_x(), y=label_img.winfo_y()+10)


def move_left(event):
    label_img.place(x=label_img.winfo_x()-10, y=label_img.winfo_y())


def move_right(event):
    label_img.place(x=label_img.winfo_x()+10, y=label_img.winfo_y())


window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

window.bind('<Up>', move_up)
window.bind('<Down>', move_down)
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)
label_img = Label(window, image=icon, width=40, height=40)

label_img.place(x=50, y=50)
# --------------------------

window.mainloop()  # place window in PC screen
