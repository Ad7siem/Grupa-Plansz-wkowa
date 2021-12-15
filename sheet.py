import gspread
from tkinter import filedialog

# Create open file json
def open_json():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", title="Wybierz plik json", filetypes=(("Json", "*.json"), ("all files", "*.*")))


# Create Open Sheet
def OpenSheet(name_sheet):
    
    try:
        gc = gspread.service_account(filename=filename)
        sh = gc.open_by_key('1FT3Jau5n1kYi3nSl1w9W3eVWmGDanUSUhsTy0XEEUjM')
    except:
        open_json()
        gc = gspread.service_account(filename=filename)
        sh = gc.open_by_key('1FT3Jau5n1kYi3nSl1w9W3eVWmGDanUSUhsTy0XEEUjM')

    worksheet = sh.worksheet(name_sheet)
    return worksheet, wc


def List_Items(name_sheet, column):

    list_items = []

    worksheet = OpenSheet(name_sheet)
    records = worksheet.get_all_values()
    
    for record in records:
        list_items.append(record[column])

    return list_items