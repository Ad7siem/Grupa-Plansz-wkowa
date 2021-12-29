# from tkinter import *
# from tkinter import ttk

# w = Tk()
# w.geometry('600x400')

# # ide = 0

# # def isChecked():
# #     kz = var2.get()
# #     if kz == 1:
# #         ide = 1
# #         print(1, ide)
# #     # elif var2 == 0:
# #     #     ide = 0
# #     #     print(0, ide)
# #     else:
# #         ide= 5
# #         print('źle')

# # def button_click():
# #     print(ide)

# # var = IntVar()
# # var2 = IntVar()
# # # info_lost_checkbutton = Checkbutton(w, text='Jeśli jest wiele osób zmywających, zaznacz przy tych osobach', variable = var, onvalue=1, offvalue=0, command=isChecked)
# # # info_lost_checkbutton.pack(side=LEFT, padx=20, pady=20)

# # Radiobutton(w, text='coś', variable=var2, value=1, command=isChecked).pack()

# # button = Button(w, text='Click', command=button_click)
# # button.pack(side=LEFT, padx=20, pady=20)

# def checkkey(event):
       
#     value = event.widget.get()
#     # print(value)
      
#     # get data from l
#     if value == '':
#         data = l
#     else:
#         data = []
#         for item in l:
#             if value.lower() in item.lower():
#                 data.append(item)                
   
#     # update data in listbox
#     update(data)
   
   
# def update(data):
      
#     # clear previous data
#     lb.delete(0, 'end')
   
#     # put new data
#     for item in data:
#         lb.insert('end', item)
  
  
# # Driver code
# l = ('C','C++','Java',
#      'Python','Perl',
#      'PHP','ASP','JS' )
  
  
# #creating text box 
# e = Entry(w)
# e.pack()
# e.bind('<KeyRelease>', checkkey)
# e.update()
  
# #creating list box
# lb = Listbox(w)
# lb.pack()
# update(l)

# w.mainloop()

'''
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *
from configparser import ConfigParser

# Read our config file and get colors
parser = ConfigParser()
parser.read('test.ini')
saved_window_background = parser.get('colors', 'window_background')

countries = [
        'Antigua and Barbuda', 'Bahamas','Barbados','Belize', 'Canada',
        'Costa Rica ', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador ',
        'Grenada', 'Guatemala ', 'Haiti', 'Honduras ', 'Jamaica', 'Mexico',
        'Nicaragua', 'Saint Kitts and Nevis', 'Panama ', 'Saint Lucia', 
        'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America'
        ]

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg=saved_window_background)

frame = Frame(ws, bg=saved_window_background)
frame.pack(expand=True)

Label(
    frame, 
    bg=saved_window_background,
    font = ('Times',21),
    text='Countries in North America '
    ).pack()

entry = AutocompleteCombobox(
    frame, 
    width=30, 
    font=('Times', 18),
    completevalues=countries
    )
entry.pack()

ws.mainloop()  
'''
from tkinter import *

w_INFO = Tk()
w_INFO.title('Informacje')
w_INFO.geometry('550x650')
w_INFO.iconbitmap('Logo klub.ico')

bg = PhotoImage(file="Images/info.png")
# bg1 = PhotoImage(file="Images/tlo.png")
# bg2 = PhotoImage(file="Images/tlo.jpg")
info = PhotoImage(file='Images/informacje.png')

test_one = Frame(w_INFO)
test_one.pack(side=TOP)
test_two = Frame(w_INFO)
test_two.pack(side=TOP)

def isCheck():
    my_button.pack()

def Show():
    print(c.get())
    my_button = Button(test_two, image=info)
    if c.get() == 1:
        my_button.pack()
    elif c.get() == 0:
        my_button.destroy() 

c = IntVar()
cb = Checkbutton(w_INFO, text='Show button', variable=c)
cb.pack()

# my_label = Label(w_INFO, image=bg)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)

my_button2 = Button(test_one, text='Zatwierdź', command=Show).pack()




w_INFO.mainloop()