from tkinter import *
from tkinter import ttk
from sheet import OpenSheet, open_ini

# Read our config file and get sheet
parser = open_ini()
sheet_all_results = parser.get('sheet', 'sheet_all_results')


# Create Table Game 
def Table_Games_Win(root, height=10): #, row=0, column=2, rowspan=1, columnspan=1, padx=10, pady=10, ipadx=0, ipady=0):
    global table_games_win

    table_games_win = ttk.Treeview(root, height=height)
    table_games_win['column']=('Place', 'Name', 'Points')
    table_games_win.column('#0', width=0, stretch=OFF)
    table_games_win.column('Place', anchor=E, width=50)
    table_games_win.column('Name', anchor=CENTER, width=100)
    table_games_win.column('Points', anchor=CENTER, width=50)
    
    table_games_win.heading('#0', text='', anchor=CENTER)
    table_games_win.heading('Place', text='Miejsce', anchor=E)
    table_games_win.heading('Name', text='Imię', anchor=CENTER)
    table_games_win.heading('Points', text='Punkty', anchor=CENTER)

    # table_games_win.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, pady=pady, padx=padx, ipadx=ipadx, ipady=ipady)
    table_games_win.pack(padx=10, pady=(5,10))


# Create Table Lost
def Table_Games_Lost(root, height=10): #, row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10, ipadx=0, ipady=0):
    global table_games_lost

    table_games_lost = ttk.Treeview(root, height=height)
    table_games_lost['column']=('Place', 'Name', 'Points')
    table_games_lost.column('#0', width=0, stretch=OFF)
    table_games_lost.column('Place', anchor=E, width=50)
    table_games_lost.column('Name', anchor=CENTER, width=100)
    table_games_lost.column('Points', anchor=CENTER, width=100)
    
    table_games_lost.heading('#0', text='', anchor=CENTER)
    table_games_lost.heading('Place', text='Miejsce', anchor=E)
    table_games_lost.heading('Name', text='Imię', anchor=CENTER)
    table_games_lost.heading('Points', text='Procent zmywań', anchor=CENTER)

    # table_games_lost.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, pady=pady, padx=padx, ipadx=ipadx, ipady=ipady)
    table_games_lost.pack(padx=10, pady=(5,10))


# Create Function Show Table
def query_list_results_game():
    worksheet = OpenSheet(sheet_all_results)

    table_games_win.delete(*table_games_win.get_children())
    table_games_win.update()
    table_games_lost.delete(*table_games_lost.get_children())
    table_games_lost.update()

    records = worksheet.get_all_values()[3:]

    for record in records:
        table_games_win.insert(parent='', index=len(records), values = (f'{record[1]} {record[2]} {record[3]}'))
        table_games_lost.insert(parent='', index=len(records), values = (f'{record[5]} {record[6]} {record[7]}'))