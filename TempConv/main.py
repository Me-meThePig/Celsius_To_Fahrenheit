from tkinter import *
from tkinter import IntVar


def on_change(*args):
    try:
        celsius = textc.get()
        # convert Celsius to Fahrenheit
        fahrenheit = (celsius * 1.8) + 32
        fntL.config(text=f"Fahrenheit: {fahrenheit:.2f}")
    except TclError:
        # handle empty or invalid input
        fntL.config(text="Fahrenheit: Invalid Input")


# app setup
root = Tk()
root.title("Temperature Converter")
root.geometry("300x100")
root.resizable(False, False)


# Celsius
textc = IntVar(root, name="int")

clsL = Label(root, text="Celsius:", font="Arial 12 bold")
clsL.place(x=5, y=10)

clsE = Entry(root, textvariable=textc, font=30, width=25)
clsE.place(x=5, y=40)


# Fahrenheit
fntL = Label(root, text=f"Fahrenheit: {textc.get()}", font="Arial 12 bold")
fntL.place(x=5, y=70)

# update Fahrenheit text
textc.trace_add("write", on_change)
on_change()


root.mainloop()
