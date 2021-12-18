from tkinter import *
from tkinter import ttk
from sheet import OpenSheet, List_Items
from ttkwidgets.autocomplete import AutocompleteCombobox


# Create Function to Add Board Game
def submit_board_game():
    global w_BG
    w_BG = Tk()
    w_BG.title('Dodawanie gry planszowej')
    w_BG.iconbitmap('Logo klub.ico')
    w_BG.geometry('320x220')
    w_BG.resizable(width=0, height=0)
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
    global w_RFD
    w_RFD = Tk()
    w_RFD.title('Dodawanie wyników dnia')
    w_RFD.geometry('550x250')
    w_RFD.resizable(width=0, height=0)
    w_RFD.iconbitmap('Logo klub.ico')
    w_RFD.config(bg='#3e3e3e')

    # print(List_Items('ID_Gry', 0)) # ====================================
    list_games = List_Items('ID_Gry', 0)
    list_players = List_Items('ID_Gracza', 0)

    global index_results_day
    global name_board_games_results_day
    global game_data_d
    global game_data_m
    global game_data_y

    # Create Result LabelFrame
    global window_with_entering_results
    window_with_entering_results = LabelFrame(w_RFD, text='Dodaj resultat dnia', bg='#3e3e3e', fg='#d3d3d3')
    window_with_entering_results.pack(padx=10, pady=10, ipady=5)

    # Create Frame First Items
    first_data = Frame(window_with_entering_results, bg='#3e3e3e')
    first_data.pack(side=TOP)

    row_one_first_data = Frame(first_data, bg='#3e3e3e')
    row_one_first_data.pack(side=TOP)
    row_two_first_data = Frame(first_data, bg='#3e3e3e')
    row_two_first_data.pack(side=TOP)

    # Create Quantity Players
    quantity_players_label = Label(row_one_first_data, text='Podaj ilość graczy w grze:', bg='#3e3e3e', fg='#d3d3d3')
    quantity_players_label.pack(side=LEFT, padx=(10,2), pady=10)

    global quantity_players_entry
    quantity_players_entry = Entry(row_one_first_data, width=3)
    quantity_players_entry.pack(side=LEFT, padx=(2,10), pady=10)

    # Create Game Data
    game_data_label = Label(row_one_first_data, text='Podaj date rozgrywki (d/m/r):', bg='#3e3e3e', fg='#d3d3d3')
    game_data_label.pack(side=LEFT, padx=10, pady=10)

    game_data_d = Entry(row_one_first_data, width=3)
    game_data_d.pack(side=LEFT, padx=(5,0), pady=10)
    first_other_text = Label(row_one_first_data, text='-', bg='#3e3e3e', fg='#d3d3d3')
    first_other_text.pack(side=LEFT, pady=10)
    game_data_m = Entry(row_one_first_data, width=3)
    game_data_m.pack(side=LEFT, padx=0, pady=10)
    second_other_text = Label(row_one_first_data, text='-', bg='#3e3e3e', fg='#d3d3d3')
    second_other_text.pack(side=LEFT, pady=10)
    game_data_y = Entry(row_one_first_data, width=5)
    game_data_y.pack(side=LEFT, padx=(0,10), pady=10)

    # Create Index Game Result in Day
    index_results_day_label = Label(row_two_first_data, text='Liczba Porządkowa:', bg='#3e3e3e', fg='#d3d3d3')
    index_results_day_label.pack(side=LEFT, padx=(10,2), pady=10)

    index_results_day = Entry(row_two_first_data, width=4)
    index_results_day.pack(side=LEFT, padx=(2,10), pady=10)

    # Create Name Game Bord
    name_board_games_results_day_label = Label(row_two_first_data, text='Nazwa gry:', bg='#3e3e3e', fg='#d3d3d3')
    name_board_games_results_day_label.pack(side=LEFT, padx=(10,2), pady=10)

    name_board_games_results_day = AutocompleteCombobox(row_two_first_data, width=40, completevalues=list_games)
    name_board_games_results_day.pack(side=LEFT, padx=(2,10), pady=10)
    # name_board_games_results_day = Entry(row_two_first_data, width=40)
    # name_board_games_results_day.pack(side=LEFT, padx=(2,10), pady=10)


    # Create Frame with Second Items
    second_data = Frame(window_with_entering_results, bg='#3e3e3e')
    second_data.pack(side=TOP)

    # Create Frame with Label Second Items
    window_label = Frame(second_data, bg='#3e3e3e')
    window_label.pack(side=TOP, padx=10, pady=(10,0))

    place_results_day_label = Label(window_label, text='Miejsce', bg='#4a4a4a', fg='#d3d3d3', width=10)
    place_results_day_label.grid(row=0, column=0)
    name_player_results_day_label = Label(window_label, text='Nazwa Gracza', bg='#4a4a4a', fg='#d3d3d3', width=20)
    name_player_results_day_label.grid(row=0, column=1)
    points_results_day_label = Label(window_label, text='Punktacja', bg='#4a4a4a', fg='#d3d3d3', width=10)
    points_results_day_label.grid(row=0, column=2)
    result_results_day_label = Label(window_label, text='Rezultat', bg='#4a4a4a', fg='#d3d3d3', width=20)
    result_results_day_label.grid(row=0, column=3)

    # Create Frame for a Table Second Items
    global window_entry
    window_entry = Frame(second_data, bg='#3e3e3e')
    window_entry.pack(side=TOP, padx=0, pady=(0, 10))

    global place_results_day
    global name_player_results_day
    global result_results_day
    global points_results_day

    global vlist
    vlist = ['Wygrana','Przegrana', 'Zmywanie']

    place_results_day = Entry(window_entry, width=12, justify=CENTER)
    place_results_day.grid(row=0, column=0)
    # name_player_results_day = Entry(window_entry, width=24, justify=CENTER)
    # name_player_results_day.grid(row=0, column=1)
    name_player_results_day = AutocompleteCombobox(window_entry, width=24, justify=CENTER, completevalues=list_players)
    name_player_results_day.grid(row=0, column=1)
    points_results_day = Entry(window_entry, width=12, justify=CENTER)
    points_results_day.grid(row=0, column=2)
    # result_results_day = ttk.Combobox(window_entry, values = vlist, width=20)
    # result_results_day.set('-')
    result_results_day = AutocompleteCombobox(window_entry, width=20, completevalues=vlist)
    result_results_day.grid(row=0, column=3)



    info_lost_Frame = Frame(window_with_entering_results, bg='#3e3e3e')
    info_lost_Frame.pack(side=TOP)


    append_button = Frame(window_with_entering_results, bg='#3e3e3e')
    append_button.pack(side=TOP)

    a_button = Button(append_button, text='Zapisz', width=20, command=append_results)
    a_button.pack(side=BOTTOM, padx=10, pady=10)

    # ================================= Test ==========================================
    global ck 
    ck = 1
    # =================================================================================

def append_results():
    id_game = 0
    id_player = 0
    id_rivalry = 0
    id_lost = 0

    worksheet = OpenSheet('ID_Gry')

    records = []
    records = worksheet.get_all_values()
    for record in records:
        if record[0].lower() == name_board_games_results_day.get().lower():
            id_game = record[1]

        # for rec in record:
        #     if rec.lower() == name_board_games_results_day.get().lower():
        #         id_game = record[1]

    worksheet = OpenSheet('ID_Gracza')

    records = []
    records = worksheet.get_all_values()
    for record in records:
        if record[0].lower() == name_player_results_day.get().lower():
            id_player = record[2]

        # for rec in record:
        #     if rec.lower() == name_player_results_day.get().lower():
        #         id_player = record[2]

    id_rivalry = int(quantity_players_entry.get()) - int(place_results_day.get()) + 1

    # =======================================================================================  BUDOWA POPRAWNEJ WARTOŚĆI ZMYWANIA ==========================================================================================

    # if int(place_results_day.get()) == int(quantity_players_entry.get()):
    #     id_lost = -1
    # else:
    #     id_lost = 1

    ''' 
    Spróbuj zrobić tak, by przy wybraniu Wygrywa wartość była 1, przy przegrywa wartość była 0, a przy zmywaniu wartość byłą -1
    '''

    worksheet = OpenSheet('Baza')
    # global ck


    # if index_results_day.get() == worksheet.row_values(len(worksheet.get_all_values()))[0]:
    #     if place_results_day.get() > worksheet.row_values(len(worksheet.get_all_values()))[4]:
    #         id_lost = -1
    #         for i in range(0, ck):
    #             print(worksheet.row_values(len(worksheet.get_all_values()))[4])
    #             if int(worksheet.row_values(len(worksheet.get_all_values()))[4]) == 1:
    #                 worksheet.update_cell(len(worksheet.get_all_values()) - i, 9, 1)
    #             else:
    #                 worksheet.update_cell(len(worksheet.get_all_values()) - i, 9, 0)

    #     else:
    #         id_lost = -1
    #         ck += 1
    # else:
    #     id_lost = -1

    # if place_results_day.get() != worksheet.row_values(len(worksheet.get_all_values()))[4]:
    #     ck = 1

    if result_results_day.get() == 'Wygrana':
        id_lost = -1
    elif result_results_day.get() == 'Przegrana':
        id_lost = 0
    elif result_results_day.get() == 'Zmywanie':
        id_lost = 1

    # print(ck)
    # =====================================================================================================================================================================================================================

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

    worksheet.append_row(temporary_list_results)

    tk = int(place_results_day.get()) + 1
    place_results_day.delete(0, END)
    place_results_day.insert(0, str(tk))
    name_player_results_day.delete(0, END)
    points_results_day.delete(0, END)
    result_results_day.delete(0, END)
