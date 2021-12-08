from tkinter import *
from sheet import OpenSheet

# Create function to Detelete Board Games
def delete_board_game():
    global w_dBG
    w_dBG = Tk()
    w_dBG.title('Usuwanie planszówki')
    w_dBG.geometry('320x120')
    w_dBG.iconbitmap('Logo klub.ico')
    w_dBG.config(bg='#3e3e3e')

    Delete_Frame = LabelFrame(w_dBG, bg='#3e3e3e')
    Delete_Frame.pack(padx=10, pady=10, side=TOP)
    
    global delete_box
    delete_box = Entry(Delete_Frame, width=10, bg='#696969', fg='#d3d3d3')
    delete_box.pack(side=RIGHT, padx=10, pady=10)

    delete_box_label = Label(Delete_Frame, text='Id planszówki do usunięcia:', bg='#3e3e3e', fg='#d3d3d3')
    delete_box_label.pack(side=LEFT, padx=10, pady=10)

    DB_Frame = Frame(w_dBG, bg='#3e3e3e')
    DB_Frame.pack(padx=10, pady=0, side=TOP)

    delete_button = Button(DB_Frame, text='Usuń planszówkę', bg='#696969', fg='#d3d3d3', activebackground='#4a4a4a', activeforeground='white', command=delete)
    delete_button.pack(padx=10, pady=10)


# Create Function in Delete Button
def delete():

    worksheet = OpenSheet()

    position = int(delete_box.get())
    length = len(worksheet.get_all_values())

    worksheet.delete_rows(int(delete_box.get()) + 1)
    while position + 1 <= length - 1:
        worksheet.update_cell(position + 1, 1 ,position)
        position += 1

    w_dBG.destroy()