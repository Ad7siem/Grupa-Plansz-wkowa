from tkinter import *
from tkinter import ttk
from sheet import OpenSheet

# Create function to update Board Game
def edit_board_game():
    global w_EBG
    global id_board_games
    w_EBG = Tk()
    w_EBG.title('Aktualizacja')
    w_EBG.geometry('300x240')


    # Create Text Box
    id_board_games = Entry(w_EBG, width=30)
    id_board_games.grid(row=0, column=1, padx=10, pady=10)

    # Create Text Box Labels
    id_board_games_label = Label(w_EBG, text='Id:')
    id_board_games_label.grid(row=0, column=0, pady=(10), padx=10)

    # Create Edit Button
    edit_btn = Button(w_EBG, text='wybierz', command=edit)
    edit_btn.grid(row=1, column=0, columnspan=2, pady=0, padx=0)
    save_btn = Button(w_EBG, text='Zapisz zmiany', command=update_button)
    save_btn.grid(row=8, column=0, columnspan=2, pady=0, padx=0)

    # Create Global Variables for next box names
    global name_board_games_edit
    global type_board_games_edit
    global min_player_edit
    global max_player_edit
    global time_games_edit
    global owner_edit

    # Create Text Boxes
    name_board_games_edit = Entry(w_EBG, width=30)
    name_board_games_edit.grid(row=2, column=1, padx=10, pady=(10,0))
    type_board_games_edit = Entry(w_EBG, width=30)
    type_board_games_edit.grid(row=3, column=1)
    min_player_edit = Entry(w_EBG, width=30)
    min_player_edit.grid(row=4, column=1)
    max_player_edit = Entry(w_EBG, width=30)
    max_player_edit.grid(row=5, column=1)
    time_games_edit = Entry(w_EBG, width=30)
    time_games_edit.grid(row=6, column=1)
    owner_edit = Entry(w_EBG, width=30)
    owner_edit.grid(row=7, column=1)

    # Create Text Box Labels
    name_board_games_label_edit = Label(w_EBG, text='Nazwa Gry:', padx=(10))
    name_board_games_label_edit.grid(row=2, column=0, pady=(5,0))
    type_board_games_label_edit = Label(w_EBG, text='Typ:')
    type_board_games_label_edit.grid(row=3, column=0)
    min_player_label_edit = Label(w_EBG, text='Min. graczy:')
    min_player_label_edit.grid(row=4, column=0)
    max_player_label_edit = Label(w_EBG, text='Max. graczy:')
    max_player_label_edit.grid(row=5, column=0)
    time_games_label_edit = Label(w_EBG, text='Czas gry:')
    time_games_label_edit.grid(row=6, column=0)
    owner_label_edit = Label(w_EBG, text='Właściciel:')
    owner_label_edit.grid(row=7, column=0)
    

# Create function in Button Edit Board Games
def edit():
    worksheet = OpenSheet()

    records = []
    records = worksheet.row_values(int(id_board_games.get()) + 1)
    name_board_games_edit.insert(0, records[1])
    type_board_games_edit.insert(0, records[2])
    min_player_edit.insert(0, records[3])
    max_player_edit.insert(0, records[4])
    time_games_edit.insert(0, records[5])
    owner_edit.insert(0, records[6])
 

 # Create function to Save Update Board Games
def update_button():
    worksheet = OpenSheet()
    worksheet.update(f'A{int(id_board_games.get())+1}:K{int(id_board_games.get())+1}', [[int(id_board_games.get()), name_board_games_edit.get(), type_board_games_edit.get(), int(min_player_edit.get()), int(max_player_edit.get()), int(time_games_edit.get()), owner_edit.get()]])

    # Close window
    w_EBG.destroy()
