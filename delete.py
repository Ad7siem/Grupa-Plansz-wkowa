from tkinter import *
from sheet import OpenSheet, open_ini
from boardgames import cursor_board_game, query_board_game

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

    if cursor_board_game() == '':
        return None
    w_dBG = Tk()
    w_dBG.title('Usuwanie planszówki')
    w_dBG.geometry('320x120')
    w_dBG.resizable(width=0, height=0)
    w_dBG.iconbitmap('Logo klub.ico')
    w_dBG.config(bg=window_background)

    Delete_Frame = LabelFrame(w_dBG, bg=window_background)
    Delete_Frame.pack(padx=10, pady=10, side=TOP, ipadx=10, ipady=10)
    
    delete_label = Label(Delete_Frame, text=f'Czy na pewno chcesz usunąc grę \n{cursor_board_game()[1]}?',bg = window_background, fg=text)
    delete_label.pack(side=TOP, pady=10, padx=10)

    yes_delete_button = Button(Delete_Frame, text='TAK', width=10, bd=0, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, command=delete)
    yes_delete_button.pack(side=LEFT, padx=(40,0), pady=10)

    no_delete_button = Button(Delete_Frame, text='NIE', width=10, bd=0, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, command=w_dBG.destroy)
    no_delete_button.pack(side=RIGHT, padx=(0,40), pady=10)

# Create Function in Delete Button
def delete():

    worksheet = OpenSheet(sheet_all_boardgame)
    try:
        length = len(worksheet.get_all_values())

        position = int(cursor_board_game()[0])
        worksheet.delete_rows(position + 1)
        while position + 1 <= length - 1:
            worksheet.update_cell(position + 1, 1 ,position)
            position += 1
        query_board_game()
        w_dBG.destroy()
    except:
        pass