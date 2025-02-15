from tkinter import *
from tkinter import ttk
from sheet import open_json, open_ini

# Read our config file and get colors, sheet
parser = open_ini()
window_border = parser.get('colors', 'window_border')
window_background = parser.get('colors', 'window_background')
text = parser.get('colors', 'text')
button_background = parser.get('colors', 'button_background')
button_activebackground = parser.get('colors', 'button_activebackground')
table_background = parser.get('colors', 'table_background')
table_border = parser.get('colors', 'table_border')
sheets_file = parser.get('sheet', 'sheets_file')
sheets_file_boardgame = parser.get('sheet', 'sheets_file_boardgame')
sheet_all_boardgame = parser.get('sheet', 'sheet_all_boardgame')
sheet_player = parser.get('sheet', 'sheet_player')
sheet_boardgame = parser.get('sheet', 'sheet_boardgame')
sheet_results = parser.get('sheet', 'sheet_results')
sheet_all_results = parser.get('sheet', 'sheet_all_results')

# class Config:
#     def __init__(self):
#         pass
    
def config_app():
    w_CA = Tk()
    w_CA.title('Ustawienia')
    w_CA.geometry('600x370')
    w_CA.resizable(width=0, height=0)
    w_CA.iconbitmap('Logo klub.ico')
    w_CA.config(bg=window_background)

    # Create Frame or LabelFrame in window
    w = LabelFrame(w_CA, text='Ustawienia', bg=window_background, fg=text)   
    w.pack(padx=10, pady=10)

    w_option = Frame(w, bg=window_background)
    w_option.pack(padx=10, pady=10)

    w_option_file_sheets = Frame(w_option, bg=window_background)
    w_option_file_sheets.pack()
    w_separator = Frame(w_option, bg=window_background)
    w_separator.pack(fill='x')
    w_option_name_sheet = Frame(w_option, bg=window_background)
    w_option_name_sheet.pack()
    w_button = Frame(w_option, bg=window_background)
    w_button.pack(pady=(20, 0))

    # Create Label/Entry File Sheets
    google_sheets_label = Label(w_option_file_sheets, text='Link do arkuszu statystyk:', bg=window_background, fg=text)
    google_sheets_label.grid(row=0, column=0, sticky=E)

    google_sheets_all_boardgames_label = Label(w_option_file_sheets, text='Link do arkuszu z planszówkami', bg=window_background, fg=text)
    google_sheets_all_boardgames_label.grid(row=1, column=0, sticky=E)

    global google_sheets
    google_sheets = Entry(w_option_file_sheets, width=100, state = DISABLED)
    google_sheets.grid(row=0, column=1, padx=10, sticky=W)

    global google_sheets_all_boardgames
    google_sheets_all_boardgames = Entry(w_option_file_sheets, width=100, state=DISABLED)
    google_sheets_all_boardgames.grid(row=1, column=1, padx=10, sticky=W)

    # Create Separator
    separator = ttk.Separator(w_separator, orient='horizontal')
    separator.pack(fill='x', pady=20)

    # Create Label/Entry Name Sheet
    id_player_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkusza z graczami: ', bg=window_background, fg=text)
    id_player_sheet_label.grid(row=1, column=0, sticky=E)

    id_game_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkusza z listą gier: ', bg=window_background, fg=text)
    id_game_sheet_label.grid(row=2, column=0, sticky=E)

    results_day_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkusza z wynikami dnia: ', bg=window_background, fg=text)
    results_day_sheet_label.grid(row=3, column=0, sticky=E)

    boardgames_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę akrusza ze spisem wszystkich planszówek', bg=window_background, fg=text)
    boardgames_sheet_label.grid(row=4, column=0, sticky=E)

    resulsts_all_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkuszu z tablicami wyników', bg=window_background, fg=text)
    resulsts_all_sheet_label.grid(row=5, column=0, sticky=E)

    global id_player_sheet
    id_player_sheet = Entry(w_option_name_sheet, state = DISABLED)
    id_player_sheet.grid(row=1, column=1, padx=10, sticky=W)
    

    global id_game_sheet
    id_game_sheet = Entry(w_option_name_sheet, state = DISABLED)
    id_game_sheet.grid(row=2, column=1, padx=10, sticky=W)


    global results_day_sheet
    results_day_sheet = Entry(w_option_name_sheet, state = DISABLED)
    results_day_sheet.grid(row=3, column=1, padx=10, sticky=W)

    global boardgames_sheet
    boardgames_sheet = Entry(w_option_name_sheet, state= DISABLED)
    boardgames_sheet.grid(row=4, column=1, padx=10, sticky=W)

    global resulsts_all_sheet
    resulsts_all_sheet = Entry(w_option_name_sheet, state= DISABLED)
    resulsts_all_sheet.grid(row=5, column=1, padx=10, sticky=W)
    

    # Create Button
    Json_Button = Button(w_button, text='Otwórz plik z uprawnieniem', width=30 , bd=0, bg=button_background, fg=text, relief="solid", activebackground=button_activebackground, activeforeground=text, command=open_json)
    Json_Button.grid(row=0, column=0, padx=10)
    global Save_Button
    Save_Button = Button(w_button, text='Zapisz', state = DISABLED, width=17 , bd=0, bg=button_background, fg=text, relief="solid", activebackground=button_activebackground, activeforeground=text, command=save_config)
    Save_Button.grid(row=0, column=1, padx=10)
    global cb
    cb = IntVar()
    cb.set(1)
    Consent_Edit = Checkbutton(w_button, 
                                text='Chcę zmienić ustawiniea', 
                                bg=window_background, 
                                activebackground=window_background, 
                                fg=text, 
                                activeforeground=text, 
                                disabledforeground=text,
                                selectcolor=window_border,
                                variable=cb, 
                                onvalue=1, 
                                offvalue=0, 
                                command=isChecked)
    Consent_Edit.grid(row=1, column=0, columnspan=2, pady=5)

    
    Info_Button = Button(w_button, text='Informacje o aplikacji', bd=0, bg=window_background, fg=text, relief="solid", activebackground=window_background, activeforeground=text, command=info)
    Info_Button.grid(row=2, column=0, pady=(20, 0))


def save_config():
    # Config file
    parser = open_ini()
    parser.set('sheet', 'sheets_file', google_sheets.get())
    parser.set('sheet', 'sheets_file_boardgame', google_sheets_all_boardgames.get())
    parser.set('sheet', 'sheet_all_boardgame', boardgames_sheet.get())
    parser.set('sheet', 'sheet_player', id_player_sheet.get())
    parser.set('sheet', 'sheet_boardgame', id_game_sheet.get())
    parser.set('sheet', 'sheet_results', results_day_sheet.get())
    parser.set('sheet', 'sheet_all_results', resulsts_all_sheet.get())

    # Save the config file
    with open('main.ini', 'w') as configfile:
        parser.write(configfile)


def isChecked():
    if cb.get() == 1:
        # test['state'] = NORMAL
        Save_Button['state'] = NORMAL
        google_sheets['state'] = NORMAL
        google_sheets.delete(0, END)
        google_sheets.insert(0, sheets_file)
        google_sheets_all_boardgames['state'] = NORMAL
        google_sheets_all_boardgames.delete(0, END)
        google_sheets_all_boardgames.insert(0, sheets_file_boardgame)
        id_player_sheet['state'] = NORMAL
        id_player_sheet.delete(0, END)       
        id_player_sheet.insert(0, sheet_player)
        id_game_sheet['state'] = NORMAL
        id_game_sheet.delete(0, END)
        id_game_sheet.insert(0, sheet_boardgame)
        results_day_sheet['state'] = NORMAL
        results_day_sheet.delete(0, END)
        results_day_sheet.insert(0, sheet_results)
        boardgames_sheet['state'] = NORMAL
        boardgames_sheet.delete(0, END)
        boardgames_sheet.insert(0, sheet_all_boardgame)
        resulsts_all_sheet['state'] = NORMAL
        resulsts_all_sheet.delete(0, END)
        resulsts_all_sheet.insert(0, sheet_all_results)
    if cb.get() == 0:
        print('teraz')
        # test['state'] = DISABLED
        # test.configure(text='Sleeping')


def info():
    w_INFO = Tk()
    w_INFO.title('Informacje')
    w_INFO.geometry('300x180')
    w_INFO.iconbitmap('Logo klub.ico')
    w_INFO.config(bg=window_background)

    

