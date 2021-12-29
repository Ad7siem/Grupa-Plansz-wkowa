import gspread
from tkinter import filedialog
from configparser import ConfigParser

# Read our config file
def open_ini(name='main.ini'):
    parser = ConfigParser()
    parser.read(name)

    return parser

# Create open file json
def open_json():
    filename = filedialog.askopenfilename(initialdir = "/", title="Wybierz plik json", filetypes=(("Json", "*.json"), ("all files", "*.*")))

    # Config file
    parser = open_ini()
    parser.set('owner', 'json', filename)
    
    # Save the config file
    with open('main.ini', 'w') as configfile:
        parser.write(configfile)

# Create Open Sheet
def OpenSheet(name_sheet):
    # Read our config file
    parser = open_ini()
    json = parser.get('owner', 'json')
    file_sheets = parser.get('sheet', 'sheets_file')

    # Read our json with sheet
    try:
        gc = gspread.service_account(filename=json)
        sh = gc.open_by_url(file_sheets)
    except:
        open_json()
        parser.read('main.ini')
        json = parser.get('owner', 'json')
        gc = gspread.service_account(filename=json)
        sh = gc.open_by_url(file_sheets)

    worksheet = sh.worksheet(name_sheet)
    return worksheet


def List_Items(name_sheet, column):

    list_items = []

    worksheet = OpenSheet(name_sheet)
    list_items = worksheet.col_values(column)
    # records = worksheet.get_all_values()
    
    # for record in records:
    #     list_items.append(record[column])

    return list_items



# def List_Players():

#     list_players = []

#     worksheet = OpenSheet('ID_Gracza')
#     records = worksheet.get_all_values()

#     for record in records:
#         list_players.append(record[0])

#     return list_players

# def List_Games():
    
#     list_games = []

#     worksheet = OpenSheet('ID_Gry')
#     records = worksheet.get_all_values()

#     for record in records:
#         list_games.append(record[0])

#     return list_games