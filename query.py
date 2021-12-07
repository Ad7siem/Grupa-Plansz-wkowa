from sheet import OpenSheet
from table import Table_Board_Game
from tkinter import *

# Create Function to List Board Game 
def query_board_game():     
    worksheet = OpenSheet()
    table_board_games.delete(*table_board_games.get_children())
    table_board_games.update()

    records = worksheet.get_all_values()
    del records[0]

    for record in records:
        table_board_games.insert(parent='', index=len(records), values=(f'{record[0]}', f'{record[1]}', f'{record[2]}', f'{record[3]}', f'{record[4]}', f'{record[5]}', f'{record[6]}'))
