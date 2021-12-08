from tkinter import *
from sheet import OpenSheet

# Create Function to Add Board Game
def submit_board_game():
    global w_BG
    w_BG = Tk()
    w_BG.title('Dodawanie gry planszowej')
    w_BG.iconbitmap('Logo klub.ico')
    w_BG.geometry('320x220')
    w_BG.config(bg='#3e3e3e')

    # Create Global Variables for next box names
    global name_board_games
    global number_of_players
    global owner
    global version_game
    global type_board_games
    global min_player
    global max_player
    global time_games

    Submit_Frame = LabelFrame(w_BG, text='', bg='#3e3e3e')
    Submit_Frame.pack(side=TOP, padx=10, pady=10, ipady=5)

    # Create Text Boxes
    name_board_games = Entry(Submit_Frame, width=30, bg='#696969', fg='#d3d3d3')
    name_board_games.grid(row=0, column=1, padx=10, pady=(10,0))
    type_board_games = Entry(Submit_Frame, width=30, bg='#696969', fg='#d3d3d3')
    type_board_games.grid(row=1, column=1)
    min_player = Entry(Submit_Frame, width=30, bg='#696969', fg='#d3d3d3')
    min_player.grid(row=2, column=1)
    max_player = Entry(Submit_Frame, width=30, bg='#696969', fg='#d3d3d3')
    max_player.grid(row=3, column=1)
    time_games = Entry(Submit_Frame, width=30, bg='#696969', fg='#d3d3d3')
    time_games.grid(row=4, column=1)
    owner = Entry(Submit_Frame, width=30, bg='#696969', fg='#d3d3d3')
    owner.grid(row=5, column=1)


    # Create Text Box Labels
    name_board_games_label = Label(Submit_Frame, text='Nazwa Gry:', padx=(10), bg='#3e3e3e', fg='#d3d3d3')
    name_board_games_label.grid(row=0, column=0, pady=(5,0))
    type_board_games_label = Label(Submit_Frame, text='Typ:', bg='#3e3e3e', fg='#d3d3d3')
    type_board_games_label.grid(row=1, column=0)
    min_player_label = Label(Submit_Frame, text='Min. graczy', bg='#3e3e3e', fg='#d3d3d3')
    min_player_label.grid(row=2, column=0)
    max_player_label = Label(Submit_Frame, text='Max. graczy', bg='#3e3e3e', fg='#d3d3d3')
    max_player_label.grid(row=3, column=0)
    time_games_label = Label(Submit_Frame, text='Czas gry', bg='#3e3e3e', fg='#d3d3d3')
    time_games_label.grid(row=4, column=0)
    owner_label = Label(Submit_Frame, text='Właściciel:', bg='#3e3e3e', fg='#d3d3d3')
    owner_label.grid(row=5, column=0)

    SB_Frame = Frame(w_BG)
    SB_Frame.pack(side=TOP, padx=10, pady=10)

    # Create a Save Button To Save new record
    save_btn = Button(SB_Frame, text='Zapisz', width=20, bg='#696969', fg='#d3d3d3', activebackground='#4a4a4a', activeforeground='white', command=save)
    save_btn.pack()

# Create Function a Save Button
def save():
    worksheet = OpenSheet()

    temporaty_list_BG = [int(len(worksheet.get_all_values())), f"{name_board_games.get()}", f'{type_board_games.get()}', int(f'{min_player.get()}'), int(f'{max_player.get()}'), int(f'{time_games.get()}'), f'{owner.get()}']
    worksheet.append_row(temporaty_list_BG)

    # Clear The Text Boxes
    name_board_games.delete(0, END)
    owner.delete(0, END)
    type_board_games.delete(0, END)
    min_player.delete(0, END)
    max_player.delete(0, END)
    time_games.delete(0, END)