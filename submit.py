from tkinter import *
from tkinter import ttk
from configparser import ConfigParser
from sheet import OpenSheet, List_Items, open_ini
from ttkwidgets.autocomplete import AutocompleteCombobox

# Read our config file
parser = open_ini()
sheet_player = parser.get('sheet', 'sheet_player')
sheet_boardgame = parser.get('sheet', 'sheet_boardgame')
sheet_results = parser.get('sheet', 'sheet_results')
window_background = parser.get('colors', 'window_background')
button_background = parser.get('colors', 'button_background')
button_activebackground = parser.get('colors', 'button_activebackground')
text = parser.get('colors', 'text')


# Create Function to Add Board Game
def submit_board_game():
    # global w_BG
    w_BG = Tk()
    w_BG.title('Dodawanie gry planszowej')
    w_BG.iconbitmap('Logo klub.ico')
    w_BG.geometry('320x220')
    w_BG.resizable(width=0, height=0)
    w_BG.config(bg=window_background)

    # Create Global Variables for next box names
    global name_board_games
    global number_of_players
    global owner
    global version_game
    global type_board_games
    global min_player
    global max_player
    global time_games

    Submit_Frame = LabelFrame(w_BG, text='', bg=window_background)
    Submit_Frame.pack(side=TOP, padx=10, pady=10, ipady=5)

    # Create Text Boxes
    name_board_games = Entry(Submit_Frame, width=30, bg=button_background, fg=text)
    name_board_games.grid(row=0, column=1, padx=10, pady=(10,0))
    type_board_games = Entry(Submit_Frame, width=30, bg=button_background, fg=text)
    type_board_games.grid(row=1, column=1)
    min_player = Entry(Submit_Frame, width=30, bg=button_background, fg=text)
    min_player.grid(row=2, column=1)
    max_player = Entry(Submit_Frame, width=30, bg=button_background, fg=text)
    max_player.grid(row=3, column=1)
    time_games = Entry(Submit_Frame, width=30, bg=button_background, fg=text)
    time_games.grid(row=4, column=1)
    owner = Entry(Submit_Frame, width=30, bg=button_background, fg=text)
    owner.grid(row=5, column=1)


    # Create Text Box Labels
    name_board_games_label = Label(Submit_Frame, text='Nazwa Gry:', padx=(10), bg=window_background, fg=text)
    name_board_games_label.grid(row=0, column=0, pady=(5,0))
    type_board_games_label = Label(Submit_Frame, text='Typ:', bg=window_background, fg=text)
    type_board_games_label.grid(row=1, column=0)
    min_player_label = Label(Submit_Frame, text='Min. graczy', bg=window_background, fg=text)
    min_player_label.grid(row=2, column=0)
    max_player_label = Label(Submit_Frame, text='Max. graczy', bg=window_background, fg=text)
    max_player_label.grid(row=3, column=0)
    time_games_label = Label(Submit_Frame, text='Czas gry', bg=window_background, fg=text)
    time_games_label.grid(row=4, column=0)
    owner_label = Label(Submit_Frame, text='Właściciel:', bg=window_background, fg=text)
    owner_label.grid(row=5, column=0)

    SB_Frame = Frame(w_BG)
    SB_Frame.pack(side=TOP, padx=10, pady=10)

    # Create a Save Button To Save new record
    save_btn = Button(SB_Frame, text='Zapisz', width=20, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, command=save)
    save_btn.pack()

# Create Function a Save Button
def save():
    worksheet = OpenSheet('Gry')

    temporaty_list_BG = [int(len(worksheet.get_all_values())), f"{name_board_games.get()}", f'{type_board_games.get()}', int(f'{min_player.get()}'), int(f'{max_player.get()}'), int(f'{time_games.get()}'), f'{owner.get()}']
    worksheet.append_row(temporaty_list_BG)

    # Clear The Text Boxes
    name_board_games.delete(0, END)
    owner.delete(0, END)
    type_board_games.delete(0, END)
    min_player.delete(0, END)
    max_player.delete(0, END)
    time_games.delete(0, END)

# Create Function append results day
def submit_results_from_day():
    # global w_RFD
    w_RFD = Tk()
    w_RFD.title('Dodawanie wyników dnia')
    w_RFD.geometry('550x570')
    # w_RFD.resizable(width=0, height=0)
    w_RFD.iconbitmap('Logo klub.ico')
    w_RFD.config(bg=window_background)

    # Create a list for name boardgames
    list_games = List_Items(sheet_boardgame, 1)

    # Create a list for name player
    list_players = List_Items(sheet_player, 1)

    global index_results_day
    global name_board_games_results_day
    global game_data_d
    global game_data_m
    global game_data_y

    window_gameplay_data_LabelFrame = LabelFrame(w_RFD, bg=window_background, fg=text)
    window_gameplay_data_LabelFrame.pack(side=TOP, padx=10, pady=10)

    window_gameplay_data = Label(window_gameplay_data_LabelFrame, bg=window_background, fg=text)
    window_gameplay_data.pack(side=TOP, padx=10, pady=10)

    window_with_gameplay_results_LabelFrame = LabelFrame(w_RFD, bg=window_background, fg=text)
    window_with_gameplay_results_LabelFrame.pack(side=TOP, padx=10, pady=10)

    window_with_gameplay_results = Label(window_with_gameplay_results_LabelFrame, bg=window_background, fg=text)
    window_with_gameplay_results.pack(side=TOP, padx=10, pady=10)

    # Create Quantity Players
    quantity_players_label = Label(window_gameplay_data, text='Podaj ilość graczy w grze:', bg=window_background, fg=text)
    quantity_players_label.grid(row=0, column=0, sticky=W)

    # global quantity_players_entry
    global quantity_players_entry
    quantity_players_entry = Entry(window_gameplay_data, width=3)
    quantity_players_entry.grid(row=0, column=1)

    # Create Game Data
    game_data_label = Label(window_gameplay_data, text='Podaj date rozgrywki (d/m/r):', bg=window_background, fg=text)
    game_data_label.grid(row=1, column=0, sticky=W)

    game_data_d = Entry(window_gameplay_data, width=3)
    game_data_d.grid(row=1, column=1)
    first_other_text = Label(window_gameplay_data, text='-', bg=window_background, fg=text)
    first_other_text.grid(row=1, column=2)
    game_data_m = Entry(window_gameplay_data, width=3)
    game_data_m.grid(row=1, column=3)
    second_other_text = Label(window_gameplay_data, text='-', bg=window_background, fg=text)
    second_other_text.grid(row=1, column=4)
    game_data_y = Entry(window_gameplay_data, width=5)
    game_data_y.grid(row=1, column=5)

    # Create Index Game Result in Day
    index_results_day_label = Label(window_gameplay_data, text='Numer rozgrywki:', bg=window_background, fg=text)
    index_results_day_label.grid(row=2, column=0, sticky=W)

    index_results_day = Entry(window_gameplay_data, width=3)
    index_results_day.grid(row=2, column=1)

    # Create Name Game Bord
    name_board_games_results_day_label = Label(window_gameplay_data, text='Nazwa gry:', bg=window_background, fg=text)
    name_board_games_results_day_label.grid(row=3, column=0, sticky=W)
    name_board_games_results_day = AutocompleteCombobox(window_gameplay_data, width=40, completevalues=list_games)
    name_board_games_results_day.grid(row=3, column=1, columnspan=60)

    # Create ...
    place_results_day_label = Label(window_with_gameplay_results, text='Miejsce', bg=button_activebackground, fg=text, width=10)
    place_results_day_label.grid(row=0, column=0)
    name_player_results_day_label = Label(window_with_gameplay_results, text='Nazwa Gracza', bg=button_activebackground, fg=text, width=20)
    name_player_results_day_label.grid(row=0, column=1)
    points_results_day_label = Label(window_with_gameplay_results, text='Punktacja', bg=button_activebackground, fg=text, width=10)
    points_results_day_label.grid(row=0, column=2)
    result_results_day_label = Label(window_with_gameplay_results, text='Rezultat', bg=button_activebackground, fg=text, width=20)
    result_results_day_label.grid(row=0, column=3)


    global place_results_day
    global name_player_results_day
    global result_results_day
    global points_results_day

    # Create a list for results of day
    # global vlist
    vlist = ['Wygrana','Przegrana', 'Zmywanie']

    # Create Entry with Label Second Items
    place_results_day = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    place_results_day.grid(row=1, column=0)
    name_player_results_day = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    name_player_results_day.grid(row=1, column=1)
    points_results_day = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    points_results_day.grid(row=1, column=2)
    result_results_day = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    result_results_day.grid(row=1, column=3)

    # place_results_day_1 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_1.grid(row=2, column=0)
    # name_player_results_day_1 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_1.grid(row=2, column=1)
    # points_results_day_1 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_1.grid(row=2, column=2)
    # result_results_day_1 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_1.grid(row=2, column=3)

    # place_results_day_2 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_2.grid(row=3, column=0)
    # name_player_results_day_2 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_2.grid(row=3, column=1)
    # points_results_day_2 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_2.grid(row=3, column=2)
    # result_results_day_2 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_2.grid(row=3, column=3)

    # place_results_day_3 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_3.grid(row=4, column=0)
    # name_player_results_day_3 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_3.grid(row=4, column=1)
    # points_results_day_3 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_3.grid(row=4, column=2)
    # result_results_day_3 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_3.grid(row=4, column=3)

    # place_results_day_4 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_4.grid(row=5, column=0)
    # name_player_results_day_4 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_4.grid(row=5, column=1)
    # points_results_day_4 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_4.grid(row=5, column=2)
    # result_results_day_4 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_4.grid(row=5, column=3)

    # place_results_day_5 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_5.grid(row=6, column=0)
    # name_player_results_day_5 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_5.grid(row=6, column=1)
    # points_results_day_5 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_5.grid(row=6, column=2)
    # result_results_day_5 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_5.grid(row=6, column=3)

    # place_results_day_6 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_6.grid(row=7, column=0)
    # name_player_results_day_6 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_6.grid(row=7, column=1)
    # points_results_day_6 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_6.grid(row=7, column=2)
    # result_results_day_6 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_6.grid(row=7, column=3)

    # place_results_day_7 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_7.grid(row=8, column=0)
    # name_player_results_day_7 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_7.grid(row=8, column=1)
    # points_results_day_7 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_7.grid(row=8, column=2)
    # result_results_day_7 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_7.grid(row=8, column=3)

    # place_results_day_8 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_8.grid(row=9, column=0)
    # name_player_results_day_8 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_8.grid(row=9, column=1)
    # points_results_day_8 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_8.grid(row=9, column=2)
    # result_results_day_8 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_8.grid(row=9, column=3)

    # place_results_day_9 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_9.grid(row=10, column=0)
    # name_player_results_day_9 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_9.grid(row=10, column=1)
    # points_results_day_9 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_9.grid(row=10, column=2)
    # result_results_day_9 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_9.grid(row=10, column=3)

    # place_results_day_10 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_10.grid(row=11, column=0)
    # name_player_results_day_10 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_10.grid(row=11, column=1)
    # points_results_day_10 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_10.grid(row=11, column=2)
    # result_results_day_10 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_10.grid(row=11, column=3)

    # place_results_day_11 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_11.grid(row=12, column=0)
    # name_player_results_day_11 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_11.grid(row=12, column=1)
    # points_results_day_11 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_11.grid(row=12, column=2)
    # result_results_day_11 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_11.grid(row=12, column=3)

    # place_results_day_12 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_12.grid(row=13, column=0)
    # name_player_results_day_12 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_12.grid(row=13, column=1)
    # points_results_day_12 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_12.grid(row=13, column=2)
    # result_results_day_12 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_12.grid(row=13, column=3)

    # place_results_day_13 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_13.grid(row=14, column=0)
    # name_player_results_day_13 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_13.grid(row=14, column=1)
    # points_results_day_13 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_13.grid(row=14, column=2)
    # result_results_day_13 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_13.grid(row=14, column=3)

    # place_results_day_14 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # place_results_day_14.grid(row=15, column=0)
    # name_player_results_day_14 = AutocompleteCombobox(window_with_gameplay_results, width=20, justify=CENTER, completevalues=list_players)
    # name_player_results_day_14.grid(row=15, column=1)
    # points_results_day_14 = Entry(window_with_gameplay_results, width=12, justify=CENTER)
    # points_results_day_14.grid(row=15, column=2)
    # result_results_day_14 = AutocompleteCombobox(window_with_gameplay_results, width=20, completevalues=vlist)
    # result_results_day_14.grid(row=15, column=3)


    # Create Button Save Results Day
    a_button = Button(w_RFD, text='Zapisz', width=20, bd=0, bg=button_background, fg=text, activebackground=button_activebackground, activeforeground=text, command=append_results)
    a_button.pack(side=BOTTOM, padx=10, pady=(0,20))


def append_results():
    id_game = 0
    id_player = 0
    id_rivalry = 0
    id_lost = 0

    # Create search a game id
    worksheet = OpenSheet(sheet_boardgame)

    cell = worksheet.find(name_board_games_results_day.get())
    row = worksheet.row_values(cell.row)
    id_game = row[1]

    # Create search a player id
    worksheet = OpenSheet(sheet_player)

    cell = worksheet.find(name_player_results_day.get())
    row = worksheet.row_values(cell.row)
    id_player = row[2]

    # Create values points
    id_rivalry = int(quantity_players_entry.get()) - int(place_results_day.get()) + 1

    # Create values lost
    worksheet = OpenSheet(sheet_results)


    if result_results_day.get() == 'Wygrana':
        id_lost = -1
    elif result_results_day.get() == 'Przegrana':
        id_lost = 0
    elif result_results_day.get() == 'Zmywanie':
        id_lost = 1

    # Create a record of values in a worksheet
    temporary_list_results = [
        int(f'{index_results_day.get()}'), 
        int(f'{id_game}'), 
        f'{name_board_games_results_day.get()}', 
        int(f'{id_player}'), 
        int(f'{place_results_day.get()}'),
        f'{name_player_results_day.get()}',
        int(f'{points_results_day.get()}'),
        int(f'{id_rivalry}'),
        int(f'{id_lost}'),
        f'{result_results_day.get()}',
        f'{game_data_d.get()}-{game_data_m.get()}-{game_data_y.get()}']
    print(temporary_list_results)


    worksheet.append_row(temporary_list_results)

    tk = int(place_results_day.get()) + 1
    place_results_day.delete(0, END)
    place_results_day.insert(0, str(tk))
    name_player_results_day.delete(0, END)
    points_results_day.delete(0, END)
    result_results_day.delete(0, END)
