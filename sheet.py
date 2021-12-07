import gspread
from tkinter import filedialog

# Create open file json
def open_json():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", title="Wybierz plik json", filetypes=(("Json", "*.json"), ("all files", "*.*")))


# Create Open Sheet
def OpenSheet():
    try:
        gc = gspread.service_account(filename=filename)
        sh = gc.open_by_key('1FT3Jau5n1kYi3nSl1w9W3eVWmGDanUSUhsTy0XEEUjM')
    except:
        open_json()
        gc = gspread.service_account(filename=filename)
        sh = gc.open_by_key('1FT3Jau5n1kYi3nSl1w9W3eVWmGDanUSUhsTy0XEEUjM')

    worksheet = sh.sheet1
    return worksheet