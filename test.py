from tkinter import *
from tkinter import ttk

w = Tk()
w.geometry('600x400')

ide = 0

def isChecked():
    kz = var2.get()
    if kz == 1:
        ide = 1
        print(1, ide)
    # elif var2 == 0:
    #     ide = 0
    #     print(0, ide)
    else:
        ide= 5
        print('źle')

def button_click():
    print(ide)

var = IntVar()
var2 = IntVar()
# info_lost_checkbutton = Checkbutton(w, text='Jeśli jest wiele osób zmywających, zaznacz przy tych osobach', variable = var, onvalue=1, offvalue=0, command=isChecked)
# info_lost_checkbutton.pack(side=LEFT, padx=20, pady=20)

Radiobutton(w, text='coś', variable=var2, value=1, command=isChecked).pack()

button = Button(w, text='Click', command=button_click)
button.pack(side=LEFT, padx=20, pady=20)

w.mainloop()