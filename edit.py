from tkinter import *
from tkinter import ttk
from sheet import OpenSheet, open_ini
from boardgames import cursor_board_game, query_board_game

# Read our config file and get sheet, color
parser = open_ini()
sheet_all_boardgame = parser.get('sheet', 'sheet_all_boardgame')
window_background = parser.get('colors', 'window_background')
button_background = parser.get('colors', 'button_background')
button_activebackground = parser.get('colors', 'button_activebackground')
text = parser.get('colors', 'text')

# Create function to update Board Game
def edit_board_game():
    if cursor_board_game() == '':
        return None
    global w_EBG
    global id_board_games
    w_EBG = Tk()
    w_EBG.title('Aktualizacja')
    w_EBG.geometry('340x220')
    w_EBG.resizable(width=0, height=0)
    w_EBG.iconbitmap('Logo klub.ico')
    w_EBG.config(bg=window_background)

    # IBG_Frame = LabelFrame(w_EBG, bg=window_background)
    # IBG_Frame.pack(side=TOP, padx=10, pady=(20,5))

    # EB_Frame = Frame(w_EBG, bg=window_background)
    # EB_Frame.pack(side=TOP, padx=10, pady=5)

    BGE_Frame = LabelFrame(w_EBG, bg=window_background)
    BGE_Frame.pack(side=TOP, padx=10, pady=15, ipady=5)

    # SB_Frame = Frame(w_EBG, bg=window_background)
    # SB_Frame.pack(side=TOP, padx=10, pady=5)


    # Create Text Box Labels
    # id_board_games_label = Label(IBG_Frame, text='Id:', bg=window_background, fg=text)
    # id_board_games_label.pack(side=LEFT, padx=10, pady=10)

    #  # Create Text Box
    # id_board_games = Entry(IBG_Frame, width=5)
    # id_board_games.pack(side=LEFT, padx=10, pady=10)

    # Create Edit Button
    # edit_btn = Button(IBG_Frame, text='Wybierz',bd=0, width=15, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, command=edit)
    # edit_btn.pack(side=RIGHT, padx=10, pady=10)
    save_btn = Button(BGE_Frame, text='Zapisz zmiany', bd=0, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, width=20, command=update_button)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    # save_btn.pack(padx=10, pady=10)

    # Create Global Variables for next box names
    global name_board_games_edit
    global type_board_games_edit
    global min_player_edit
    global max_player_edit
    global time_games_edit
    global owner_edit

    # Create Text Boxes
    name_board_games_edit = Entry(BGE_Frame, width=30)
    name_board_games_edit.grid(row=0, column=1, padx=10, pady=(8,0))
    type_board_games_edit = Entry(BGE_Frame, width=30)
    type_board_games_edit.grid(row=1, column=1)
    min_player_edit = Entry(BGE_Frame, width=30)
    min_player_edit.grid(row=2, column=1)
    max_player_edit = Entry(BGE_Frame, width=30)
    max_player_edit.grid(row=3, column=1)
    time_games_edit = Entry(BGE_Frame, width=30)
    time_games_edit.grid(row=4, column=1)
    owner_edit = Entry(BGE_Frame, width=30)
    owner_edit.grid(row=5, column=1)


    # Create Text Box Labels
    name_board_games_label_edit = Label(BGE_Frame, text='Nazwa Gry:', padx=(10), bg=window_background, fg=text)
    name_board_games_label_edit.grid(row=0, column=0, pady=(8,0))
    type_board_games_label_edit = Label(BGE_Frame, text='Typ:', bg=window_background, fg=text)
    type_board_games_label_edit.grid(row=1, column=0)
    min_player_label_edit = Label(BGE_Frame, text='Min. graczy', bg=window_background, fg=text)
    min_player_label_edit.grid(row=2, column=0)
    max_player_label_edit = Label(BGE_Frame, text='Max. graczy', bg=window_background, fg=text)
    max_player_label_edit.grid(row=3, column=0)
    time_games_label_edit = Label(BGE_Frame, text='Czas gry', bg=window_background, fg=text)
    time_games_label_edit.grid(row=4, column=0)
    owner_label_edit = Label(BGE_Frame, text='Właściciel:', bg=window_background, fg=text)
    owner_label_edit.grid(row=5, column=0)

    values = cursor_board_game()
    # print(int(cursor_board_game()[0]))

    # id_board_games.insert(0, values[0])
    name_board_games_edit.insert(0, values[1])
    type_board_games_edit.insert(0, values[2])
    min_player_edit.insert(0, values[3])
    max_player_edit.insert(0, values[4])
    time_games_edit.insert(0, values[5])
    owner_edit.insert(0, values[6])
    

# Create function in Button Edit Board Games
# def edit():

#     name_board_games_edit.delete(0, END)
#     type_board_games_edit.delete(0, END)
#     min_player_edit.delete(0, END)
#     max_player_edit.delete(0, END)
#     time_games_edit.delete(0, END)
#     owner_edit.delete(0, END)


#     worksheet = OpenSheet(sheet_all_boardgame)

#     records = []
#     try:
#         records = worksheet.row_values(int(id_board_games.get()) + 1)
#         name_board_games_edit.insert(0, records[1])
#         type_board_games_edit.insert(0, records[2])
#         min_player_edit.insert(0, records[3])
#         max_player_edit.insert(0, records[4])
#         time_games_edit.insert(0, records[5])
#         owner_edit.insert(0, records[6])
#     except:
#         pass
 

 # Create function to Save Update Board Games
def update_button():
    worksheet = OpenSheet(sheet_all_boardgame)
    try:
        worksheet.update(f'A{int(cursor_board_game()[0])+1}:K{int(cursor_board_game()[0])+1}', [[cursor_board_game()[0], name_board_games_edit.get(), type_board_games_edit.get(), int(min_player_edit.get()), int(max_player_edit.get()), int(time_games_edit.get()), owner_edit.get()]])
        query_board_game()
        # Close window
        w_EBG.destroy()
    except:
        pass
