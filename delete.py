from tkinter import *
from sheet import OpenSheet, open_ini

# Read our config file and get sheet, color
parser = open_ini()
sheet_all_boardgame = parser.get('sheet', 'sheet_all_boardgame')
window_background = parser.get('colors', 'window_background')
button_background = parser.get('colors', 'button_background')
button_activebackground = parser.get('colors', 'button_activebackground')
text = parser.get('colors', 'text')

# Create function to Detelete Board Games
def delete_board_game():
    global w_dBG
    w_dBG = Tk()
    w_dBG.title('Usuwanie planszówki')
    w_dBG.geometry('320x120')
    w_dBG.resizable(width=0, height=0)
    w_dBG.iconbitmap('Logo klub.ico')
    w_dBG.config(bg=window_background)

    Delete_Frame = LabelFrame(w_dBG, bg=window_background)
    Delete_Frame.pack(padx=10, pady=10, side=TOP)
    
    global delete_box
    delete_box = Entry(Delete_Frame, width=10, bg=button_background, fg=window_background)
    delete_box.pack(side=RIGHT, padx=10, pady=10)

    delete_box_label = Label(Delete_Frame, text='Id planszówki do usunięcia:', bg=window_background, fg=text)
    delete_box_label.pack(side=LEFT, padx=10, pady=10)

    DB_Frame = Frame(w_dBG, bg=window_background)
    DB_Frame.pack(padx=10, pady=0, side=TOP)

    delete_button = Button(DB_Frame, text='Usuń planszówkę', width=17, bd=0, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, command=delete)
    delete_button.pack(padx=10, pady=10)


# Create Function in Delete Button
def delete():

    worksheet = OpenSheet(sheet_all_boardgame)
    try:
        position = int(delete_box.get())
        length = len(worksheet.get_all_values())

        worksheet.delete_rows(int(delete_box.get()) + 1)
        while position + 1 <= length - 1:
            worksheet.update_cell(position + 1, 1 ,position)
            position += 1

        w_dBG.destroy()
    except:
        pass