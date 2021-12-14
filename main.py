from tkinter import *
from tkinter import ttk
from boardgames import *
from resultsgame import *
from submit import submit_board_game, submit_results_from_day
from edit import edit_board_game
from delete import delete_board_game
# from query import *

color_bg = '#3e3e3e' #'#9C9CA6'
color_other = '#212121'

color = '#212121'
color_button = '#4a4a4a'
color_text = '#d3d3d3'
color_tables = '#696969'

# Creat App Window
test = Tk()
test.title('Grupa Planszówkowa')
test.geometry('1120x910')
test.config(bg=color_other)
test.iconbitmap('Logo klub.ico')
test.resizable(width=0, height=0)

# # Add some style
style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview', 
    background=color_tables,
    foreground=color_text,
    rowheight=20,
    fieldbackground=color_tables,
    lightcolor=color,
    bordercolor=color_bg,
    darkcolor=color
)
style.configure('Treeview.Heading',
    background=color_bg,
    foreground=color_text, 
    frameground=color,
    borderwidth=1,
    lightcolor=color,
    bordercolor=color_button,
    darkcolor=color
    )
style.configure("Vertical.TScrollbar", gripcount=0,
    background=color_button, darkcolor=color_button, lightcolor=color_button,
    troughcolor=color_other, bordercolor=color_other, arrowcolor=color_other
    )
style.map('Treeview',
    background=[('selected', 'silver')],
    foreground=[('selected', 'black')])
style.map('Treeview.Heading',
    background=[('selected', 'silver')],
    foreground=[('selected', 'black')])
style.map("Vertical.TScrollbar",
    background=[('selected', '#a0a000')])


# Create Main Window
window_frame = Frame(test, bg=color_bg)
window_frame.pack(padx=10, pady=17)

# Create Button Frame
Buttons_Label = Frame(window_frame, bg=color_bg)
Buttons_Label.grid(row=0, column=0, padx=10)

Buttons_Game_Board = LabelFrame(Buttons_Label, text='Gry Planszowe', bg=color_bg, fg=color_text)
Buttons_Game_Board.pack(side=TOP, pady=5, ipady=5)

Buttons_List_Resultat = LabelFrame(Buttons_Label, text='Tabela wyników', bg=color_bg, fg=color_text)
Buttons_List_Resultat.pack(side=TOP, pady=5, ipady=5)

Button_Search_Items = LabelFrame(Buttons_Label, text='Wyszukiwanie', bg=color_bg, fg=color_text)
Button_Search_Items.pack(side=TOP, pady=5, ipady=5)

# Create Table Board Games Frame 
Table_Board_Games_Label = LabelFrame(window_frame, text='Tabela Gier Planszowych', bg=color_bg, fg=color_text)
Table_Board_Games_Label.grid(row=0, column=1, rowspan=10, padx=10, pady=10)

Table_Board_Game(Table_Board_Games_Label, height=40)

# Create Table Resuls Frame
Table_Resultat_Label = Frame(window_frame, bg=color_bg)
Table_Resultat_Label.grid(row=0, column=2, rowspan=10, padx=10)

Table_Resultat_Games_Label = LabelFrame(Table_Resultat_Label, text='Rywalizacja', bg=color_bg, fg=color_text)
Table_Resultat_Games_Label.pack(side=TOP, pady=5)

Table_Games_Win(Table_Resultat_Games_Label, height=18)

Table_Games_Lost_Label = LabelFrame(Table_Resultat_Label, text='Złoty Talerz', bg=color_bg, fg=color_text)
Table_Games_Lost_Label.pack(side=TOP, pady=5)

Table_Games_Lost(Table_Games_Lost_Label, height=18)


# Create a Query Button Boards Games
querry_btn_board_games = Button(
    Buttons_Game_Board, text='Pokaż listę gier', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white' , command=query_board_game)
querry_btn_board_games.pack(padx=10, pady=(10,2))

# Create Submit Button Board Games
submit_btn_board_games = Button(
    Buttons_Game_Board, text='Dodaj planszówkę', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white', command=submit_board_game)
submit_btn_board_games.pack(padx=10, pady=2)

# Create an Update Button Board Game
edit_btn_board_game = Button(
    Buttons_Game_Board, text='Edytuj planszówkę', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white', command=edit_board_game)
edit_btn_board_game.pack(padx=10, pady=2)

# Create A Delete Button
delete_btn_board_game = Button(
    Buttons_Game_Board, text='Usuń planszówkę', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white', command=delete_board_game)
delete_btn_board_game.pack(padx=10, pady=2)

# Create a Query Button Results days
query_btn_list_results_days = Button(
    Buttons_List_Resultat, text='Pokaż wyniki', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white', command=query_list_results_game)
query_btn_list_results_days.pack(padx=10, pady=(10,2))

# Create Submit Button Result day
submit_btn_result_day = Button(
    Buttons_List_Resultat, text='Dodaj wyniki z dnia', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white', command=submit_results_from_day)
submit_btn_result_day.pack(padx=10, pady=2)

# Create an Update Button Results Day
edit_btn_results_day = Button(
    Buttons_List_Resultat, text='Pokaż wyniki z dnia', width=17, bd=0, bg=color_tables, fg=color_text, relief="solid", activebackground=color_button, activeforeground='white')
edit_btn_results_day.pack(padx=10, pady=2)

# Create Search Option
search_entry(Button_Search_Items)
search_btn = Button(
    Button_Search_Items, text='Szukaj', width=17, bd=0, bg=color_tables, fg=color_text, relief='solid', activebackground=color_button, activeforeground='white', command=search_item)
search_btn.pack(padx=10, pady=2)

test.mainloop()