from tkinter import *
from tkinter import ttk
from sheet import OpenSheet, open_ini

# Read our config file and get sheet, color
parser = open_ini()
sheet_all_boardgame = parser.get('sheet', 'sheet_all_boardgame')
window_background = parser.get('colors', 'window_background')

# Create Table Board Games
def Table_Board_Game(root, height=10): #, row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10, ipadx=0, ipady=0):   
    global table_board_games

    table_frame = Frame(root, bg=window_background)
    table_frame.pack()

    table_board_games = ttk.Treeview(table_frame, height=height)
    table_board_games.pack(side=LEFT, padx=(10, 0), pady=(5,10))


    table_board_games['columns']=('Id', 'Name', 'Type', 'MinPlayers','MaxPlayers', 'Time', 'Owner')
    table_board_games.column('#0', width=0, stretch=NO)
    table_board_games.column('Id', anchor=E, width=30)
    table_board_games.column('Name', anchor=W, width=200)
    table_board_games.column('Type', anchor=E, width=30)
    table_board_games.column('MinPlayers', anchor=E, width=70)
    table_board_games.column('MaxPlayers', anchor=E, width=70)
    table_board_games.column('Time', anchor=E, width=60)
    table_board_games.column('Owner', anchor=W, width=100)

    table_board_games.heading('#0', text='', anchor=CENTER)
    table_board_games.heading('Id', text='Id.', anchor=E)
    table_board_games.heading('Name', text='Gra Planszowa', anchor=W)
    table_board_games.heading('Type', text='Typ', anchor= E)
    table_board_games.heading('MinPlayers', text='Min graczy', anchor= E)
    table_board_games.heading('MaxPlayers', text='Max graczy', anchor= E)
    table_board_games.heading('Time', text='Czas gry', anchor= E)
    table_board_games.heading('Owner', text='Właściciel', anchor=W)

    sb = ttk.Scrollbar(table_frame, orient=VERTICAL)
    sb.pack(side=LEFT, fill=Y, padx=(0,10), pady=(6,11))
    table_board_games.config(yscrollcommand=sb.set)
    sb.config(command=table_board_games.yview)

    # table_board_games.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
    

# Create Function to List Board Game 
def query_board_game():     
    worksheet = OpenSheet(sheet_all_boardgame)
    table_board_games.delete(*table_board_games.get_children())
    table_board_games.update()

    records = worksheet.get_all_values()
    del records[0]

    for record in records:
        table_board_games.insert(parent='', index=len(records), values=(f'{record[0]}', f'{record[1]}', f'{record[2]}', f'{record[3]}', f'{record[4]}', f'{record[5]}', f'{record[6]}'))


def search_entry(root):
    global s_entry
    s_entry = Entry(root)#, bg='#696969', fg='white')
    s_entry.pack(padx=10, pady=(10,2))


def search_item():
    worksheet = OpenSheet(sheet_all_boardgame)
    table_board_games.delete(*table_board_games.get_children())
    table_board_games.update()
    
    records = []
    records = worksheet.get_all_values()
    for record in records:
        for rec in record:
            if rec.upper() == s_entry.get().upper():
                table_board_games.insert(parent='', index=END, values=(f'{record[0]}', f'{record[1]}', f'{record[2]}', f'{record[3]}', f'{record[4]}', f'{record[5]}', f'{record[6]}'))
    

def cursor_board_game():
    selected = table_board_games.focus()
    values = table_board_games.item(selected, 'values')
    return values

def bind_board_games():
    table_board_games.bind("<ButtonRelease-1>", cursor_board_game)