from tkinter import *
from sheet import OpenSheet

# Create Function to Add Board Game
def submit_board_game():
    global w_BG
    w_BG = Tk()
    w_BG.title('Dodawanie gry planszowej')
    w_BG.geometry('300x180')

    # Create Global Variables for next box names
    global name_board_games
    global number_of_players
    global owner
    global version_game
    global type_board_games
    global min_player
    global max_player
    global time_games

    # Create Text Boxes
    name_board_games = Entry(w_BG, width=30)
    name_board_games.grid(row=0, column=1, padx=10, pady=(10,0))
    type_board_games = Entry(w_BG, width=30)
    type_board_games.grid(row=1, column=1)
    min_player = Entry(w_BG, width=30)
    min_player.grid(row=2, column=1)
    max_player = Entry(w_BG, width=30)
    max_player.grid(row=3, column=1)
    time_games = Entry(w_BG, width=30)
    time_games.grid(row=4, column=1)
    owner = Entry(w_BG, width=30)
    owner.grid(row=5, column=1)


    # Create Text Box Labels
    name_board_games_label = Label(w_BG, text='Nazwa Gry:', padx=(10))
    name_board_games_label.grid(row=0, column=0, pady=(5,0))
    type_board_games_label = Label(w_BG, text='Typ:')
    type_board_games_label.grid(row=1, column=0)
    min_player_label = Label(w_BG, text='Min. graczy')
    min_player_label.grid(row=2, column=0)
    max_player_label = Label(w_BG, text='Max. graczy')
    max_player_label.grid(row=3, column=0)
    time_games_label = Label(w_BG, text='Czas gry')
    time_games_label.grid(row=4, column=0)
    owner_label = Label(w_BG, text='Właściciel:')
    owner_label.grid(row=5, column=0)

    # Create a Save Button To Save new record
    save_btn = Button(w_BG, text='Zapisz', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

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