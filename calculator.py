from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text+str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""
def erase():
    global equation_text
    n = len(equation_text)
    k = equation_text[:n-1]
    equation_label.set(k)
    equation_text = equation_text[:n-1]


window = Tk()
window.title("Ashwin's Calculator")
window.geometry("500x500")
window.config(bg="black")

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=('consolas',20),bg="white",fg="green",width=24,height=2)
label.pack()

frame = Frame(window)
frame.pack()

but1 = Button(frame,text=1,height=4,width=9,font=35,command=lambda: button_press(1),bg="black",fg="green")
but1.grid(row=0, column=0)

but2 = Button(frame,text=2,height=4,width=9,font=35,command=lambda: button_press(2),bg="black",fg="green")
but2.grid(row=0, column=1)

but3 = Button(frame,text=3,height=4,width=9,font=35,command=lambda: button_press(3),bg="black",fg="green")
but3.grid(row=0, column=2)

but4 = Button(frame, text=4, height=4, width=9, font=35,command=lambda: button_press(4),bg="black",fg="green")
but4.grid(row=1, column=0)

but5 = Button(frame, text=5, height=4, width=9, font=35,command=lambda: button_press(5),bg="black",fg="green")
but5.grid(row=1, column=1)

but6 = Button(frame, text=6, height=4, width=9, font=35,command=lambda: button_press(6),bg="black",fg="green")
but6.grid(row=1, column=2)

but7 = Button(frame, text=7, height=4, width=9, font=35,command=lambda: button_press(7),bg="black",fg="green")
but7.grid(row=2, column=0)

but8 = Button(frame, text=8, height=4, width=9, font=35,command=lambda: button_press(8),bg="black",fg="green")
but8.grid(row=2, column=1)

but9 = Button(frame, text=9, height=4, width=9, font=35,command=lambda: button_press(9),bg="black",fg="green")
but9.grid(row=2, column=2)

but10 = Button(frame, text=0, height=4, width=9, font=35,command=lambda: button_press(0),bg="black",fg="green")
but10.grid(row=3, column=0)


plus = Button(frame, text='+', height=4, width=9, font=35,command=lambda: button_press('+'),bg="black",fg="green")
plus.grid(row=0, column=3)
minus = Button(frame, text='-', height=4, width=9, font=35,command=lambda: button_press('-'),bg="black",fg="green")
minus.grid(row=1, column=3)
multiply = Button(frame, text='*', height=4, width=9, font=35,command=lambda: button_press('*'),bg="black",fg="green")
multiply.grid(row=2, column=3)
divide = Button(frame, text='/', height=4, width=9, font=35,command=lambda: button_press('/'),bg="black",fg="green")
divide.grid(row=3, column=3)
equal = Button(frame, text='=', height=4, width=9, font=35,command=equals,bg="black",fg="green")
equal.grid(row=3, column=2)
decimal = Button(frame, text='.', height=4, width=9, font=35,command=lambda: button_press('.'),bg="black",fg="green")
decimal.grid(row=3, column=1)
clear = Button(window, text='clear', height=4, width=12, font=35,command=clear,bg="black",fg="green")
clear.pack()
delete = Button(window, text='back', height=4, width=12, font=35,command=erase,bg="black",fg="green")
delete.pack()
window.mainloop()
