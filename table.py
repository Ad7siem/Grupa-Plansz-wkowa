from tkinter import *
from tkinter import ttk
from sheet import OpenSheet


def Table_Board_Game(root, height=10): #, row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10, ipadx=0, ipady=0):   
    global table_board_games

    table_frame = Frame(root, bg='#3e3e3e')
    table_frame.pack()

    # table_scroll = Scrollbar(table_frame)
    # table_scroll.pack(side=RIGHT, fill=Y)

    table_board_games = ttk.Treeview(table_frame, height=height) #, yscrollcommand=table_scroll.set)
    table_board_games.pack(side=LEFT, padx=(10, 0), pady=(5,10))
    # table_scroll.config(command=table_board_games.yview())

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


# Create Function to List Board Game 
def query_board_game():     
    worksheet = OpenSheet()
    table_board_games.delete(*table_board_games.get_children())
    table_board_games.update()

    records = worksheet.get_all_values()
    del records[0]

    for record in records:
        table_board_games.insert(parent='', index=len(records), values=(f'{record[0]}', f'{record[1]}', f'{record[2]}', f'{record[3]}', f'{record[4]}', f'{record[5]}', f'{record[6]}'))

