import tkinter
from tkinter import *

def show(value):
    global equation
    equation += value
    Label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    Label_result.config(text=result)

def create_gui():
    global root, Label_result, equation
    equation = ""

    root = Tk()
    root.title("Asad's Calculator")
    root.geometry("400x600+100+200")
    root.resizable(False, False)
    root.configure(bg="#2d2d2d")

    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 24), bg="#2d2d2d", fg="#ffffff", anchor="e")
    Label_result.pack(pady=20)

    button_frame = Frame(root, bg="#2d2d2d")
    button_frame.pack()

    button_config = {
        "width": 5,
        "height": 2,
        "font": ("Arial", 18, "bold"),
        "bd": 1,
        "fg": "#ffffff",
        "activebackground": "#555555",
        "relief": FLAT,
    }

    buttons = [
        ("C", 1, 0, "#ff5c5c", clear, 1),
        ("/", 1, 1, "#5c5cff", lambda: show("/"), 1),
        ("%", 1, 2, "#5c5cff", lambda: show("%"), 1),
        ("*", 1, 3, "#5c5cff", lambda: show("*"), 1),
        ("7", 2, 0, "#3e3e3e", lambda: show("7"), 1),
        ("8", 2, 1, "#3e3e3e", lambda: show("8"), 1),
        ("9", 2, 2, "#3e3e3e", lambda: show("9"), 1),
        ("-", 2, 3, "#5c5cff", lambda: show("-"), 1),
        ("4", 3, 0, "#3e3e3e", lambda: show("4"), 1),
        ("5", 3, 1, "#3e3e3e", lambda: show("5"), 1),
        ("6", 3, 2, "#3e3e3e", lambda: show("6"), 1),
        ("+", 3, 3, "#5c5cff", lambda: show("+"), 1),
        ("1", 4, 0, "#3e3e3e", lambda: show("1"), 1),
        ("2", 4, 1, "#3e3e3e", lambda: show("2"), 1),
        ("3", 4, 2, "#3e3e3e", lambda: show("3"), 1),
        ("0", 5, 0, "#3e3e3e", lambda: show("0"), 1),
        (".", 5, 2, "#3e3e3e", lambda: show("."), 1),
        ("=", 4, 3, "#00cc66", calculate, 2)
    ]

    for (text, row, col, color, command, rowspan) in buttons:
        button = Button(button_frame, text=text, bg=color, command=command, **button_config)
        button.config(bg=color)
        button.grid(row=row, column=col, padx=5, pady=5, rowspan=rowspan)

    Button(button_frame, text="0", width=11, height=2, font=("Arial", 18, "bold"), bd=1, fg="#ffffff", bg="#3e3e3e",
           activebackground="#555555", relief=FLAT, command=lambda: show("0")).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()
