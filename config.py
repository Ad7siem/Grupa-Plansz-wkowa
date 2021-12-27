from tkinter import *
from tkinter import ttk
from configparser import ConfigParser
from sheet import open_json

# class Config:
#     def __init__(self):
#         pass
    
def config_app():
    w_CA = Tk()
    w_CA.title('Ustawienia')
    w_CA.geometry('600x500')
    w_CA.resizable(width=0, height=0)
    w_CA.iconbitmap('Logo klub.ico')
    w_CA.config(bg='#3e3e3e')

    # Read our config file and get colors
    parser = ConfigParser()
    parser.read('main.ini')
    window_border = parser.get('colors', 'window_border')
    window_background = parser.get('colors', 'window_background')
    text = parser.get('colors', 'text')
    button_background = parser.get('colors', 'button_background')
    button_activebackground = parser.get('colors', 'button_activebackground')
    table_background = parser.get('colors', 'table_background')
    table_border = parser.get('colors', 'table_border')

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
    google_sheets_label = Label(w_option_file_sheets, text='Podaj link do pliku:', bg=window_background, fg=text)
    google_sheets_label.grid(row=0, column=0, sticky=E)

    global google_sheets
    google_sheets = Entry(w_option_file_sheets, width=100)
    google_sheets.grid(row=0, column=1, padx=10, sticky=W)

    # Create Separator
    separator = ttk.Separator(w_separator, orient='horizontal')
    separator.pack(fill='x', pady=20)

    # Create Label/Entry Name Sheet
    id_player_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkusza z graczami: ', bg=window_background, fg=text)
    id_player_sheet_label.grid(row=1, column=0, sticky=E)

    id_game_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkusza z grami: ', bg=window_background, fg=text)
    id_game_sheet_label.grid(row=2, column=0, sticky=E)

    results_day_sheet_label = Label(w_option_name_sheet, text='Podaj nazwę arkusza z wynikami dnia: ', bg=window_background, fg=text)
    results_day_sheet_label.grid(row=3, column=0, sticky=E)

    global id_player_sheet
    id_player_sheet = Entry(w_option_name_sheet)
    id_player_sheet.grid(row=1, column=1, padx=10, sticky=W)

    global id_game_sheet
    id_game_sheet = Entry(w_option_name_sheet)
    id_game_sheet.grid(row=2, column=1, padx=10, sticky=W)

    global results_day_sheet
    results_day_sheet = Entry(w_option_name_sheet)
    results_day_sheet.grid(row=3, column=1, padx=10, sticky=W)

    # Create Button
    Json_Button = Button(w_button, text='Otwórz plik z uprawnieniem', width=30 , bd=0, bg=button_background, fg=text, relief="solid", activebackground=button_activebackground, activeforeground='white', command=open_json)
    Json_Button.grid(row=0, column=0, padx=10)
    Save_Button = Button(w_button, text='Zapisz', width=17 , bd=0, bg=button_background, fg=text, relief="solid", activebackground=button_activebackground, activeforeground='white', command=save_config)
    Save_Button.grid(row=0, column=1, padx=10)
    Info_Button = Button(w_button, text='Informacje o aplikacji', bd=0, bg=window_background, fg=text, relief="solid", activebackground=window_background, activeforeground=text)
    Info_Button.grid(row=1, column=0, pady=(20, 0))

def save_config():
    # Config file
    parser = ConfigParser()
    parser.read('main.ini')
    parser.set('sheet', 'sheets_file', google_sheets.get())
    parser.set('sheet', 'sheet_player', id_player_sheet.get())
    parser.set('sheet', 'sheet_boardgame', id_game_sheet.get())
    parser.set('sheet', 'sheet_results', results_day_sheet.get())

    # Save the config file
    with open('main.ini', 'w') as configfile:
        parser.write(configfile)

