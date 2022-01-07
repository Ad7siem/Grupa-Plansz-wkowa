from tkinter import *
from tkinter import ttk
from boardgames import *
from resultsgame import *
from submit import submit_board_game, submit_results_from_day
from edit import edit_board_game
from delete import delete_board_game
from config import config_app
from sheet import open_ini
# from query import *

# Read our config file and get colors
parser = open_ini()
window_border = parser.get('colors', 'window_border')
window_background = parser.get('colors', 'window_background')
text = parser.get('colors', 'text')
button_background = parser.get('colors', 'button_background')
button_activebackground = parser.get('colors', 'button_activebackground')
table_background = parser.get('colors', 'table_background')
table_border = parser.get('colors', 'table_border')

# Creat App Window
test = Tk()
test.title('Grupa Planszówkowa')
test.geometry('1120x910')
test.config(bg=window_border)
test.iconbitmap('Logo klub.ico')
test.resizable(width=0, height=0)

# # Add some style
style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview', 
    background=table_background,
    foreground=text,
    rowheight=20,
    fieldbackground=table_background,
    lightcolor=table_border,
    bordercolor=window_background,
    darkcolor=table_border
)
style.configure('Treeview.Heading',
    background=window_background,
    foreground=text, 
    frameground=table_border,
    borderwidth=1,
    lightcolor=table_border,
    bordercolor=table_background,
    darkcolor=table_border
    )
style.configure("Vertical.TScrollbar", gripcount=0,
    background=window_background, darkcolor=window_background, lightcolor=window_background,
    troughcolor=window_border, bordercolor=window_border, arrowcolor=window_border
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
window_frame = Frame(test, bg=window_background)
window_frame.pack(padx=10, pady=17)

# Create Button Frame
Buttons_Label = Frame(window_frame, bg=window_background)
Buttons_Label.grid(row=0, column=0, padx=10)

Buttons_Game_Board = LabelFrame(Buttons_Label, text='Gry Planszowe', bg=window_background, fg=text)
Buttons_Game_Board.pack(side=TOP, pady=5, ipady=5)

Buttons_List_Resultat = LabelFrame(Buttons_Label, text='Tabela wyników', bg=window_background, fg=text)
Buttons_List_Resultat.pack(side=TOP, pady=5, ipady=5)

Button_Search_Items = LabelFrame(Buttons_Label, text='Wyszukiwanie', bg=window_background, fg=text)
Button_Search_Items.pack(side=TOP, pady=5, ipady=5)

Button_Info_App = Frame(Buttons_Label, bg=window_background)
Button_Info_App.pack(side=BOTTOM, pady=(20, 5), ipady=5)

Button_Add_File = LabelFrame(Buttons_Label, text='Opcje', bg=window_background, fg=text)
Button_Add_File.pack(side=BOTTOM, pady=(300, 5), ipady=5)


# Create Table Board Games Frame 
Table_Board_Games_Label = LabelFrame(window_frame, text='Tabela Gier Planszowych', bg=window_background, fg=text)
Table_Board_Games_Label.grid(row=0, column=1, rowspan=10, padx=10, pady=10)

Table_Board_Game(Table_Board_Games_Label, height=40)


# Create Table Resuls Frame
Table_Resultat_Label = Frame(window_frame, bg=window_background)
Table_Resultat_Label.grid(row=0, column=2, rowspan=10, padx=10)

Table_Resultat_Games_Label = LabelFrame(Table_Resultat_Label, text='Rywalizacja', bg=window_background, fg=text)
Table_Resultat_Games_Label.pack(side=TOP, pady=5)

Table_Games_Win(Table_Resultat_Games_Label, height=18)

Table_Games_Lost_Label = LabelFrame(Table_Resultat_Label, text='Złoty Talerz', bg=window_background, fg=text)
Table_Games_Lost_Label.pack(side=TOP, pady=5)

Table_Games_Lost(Table_Games_Lost_Label, height=18)


# Create a Query Button Boards Games
querry_btn_board_games = Button(
        Buttons_Game_Board, 
        text='Pokaż listę gier', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=query_board_game)
querry_btn_board_games.pack(padx=10, pady=(10,2))

# Create Submit Button Board Games
submit_btn_board_games = Button(
        Buttons_Game_Board, 
        text='Dodaj planszówkę', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=submit_board_game)
submit_btn_board_games.pack(padx=10, pady=2)

# Create an Update Button Board Game
edit_btn_board_game = Button(
        Buttons_Game_Board, 
        text='Edytuj planszówkę', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=edit_board_game)
edit_btn_board_game.pack(padx=10, pady=2)

# Create A Delete Button
delete_btn_board_game = Button(
        Buttons_Game_Board, 
        text='Usuń planszówkę', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=delete_board_game)
delete_btn_board_game.pack(padx=10, pady=2)

# Create a Query Button Results days
query_btn_list_results_days = Button(
        Buttons_List_Resultat, 
        text='Pokaż wyniki', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=query_list_results_game)
query_btn_list_results_days.pack(padx=10, pady=(10,2))

# Create Submit Button Result day
submit_btn_result_day = Button(
        Buttons_List_Resultat, 
        text='Dodaj wyniki z dnia', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=submit_results_from_day)
submit_btn_result_day.pack(padx=10, pady=2)

# Create an Update Button Results Day
edit_btn_results_day = Button(
        Buttons_List_Resultat, 
        text='Pokaż wyniki z dnia', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief="solid", 
        activebackground=button_activebackground, 
        activeforeground=text)
edit_btn_results_day.pack(padx=10, pady=2)

# Create Search Option
search_entry(Button_Search_Items)
search_btn = Button(
        Button_Search_Items, 
        text='Szukaj', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief='solid', 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=search_item)
search_btn.pack(padx=10, pady=2)

# Create Config
add_json = Button(
        Button_Add_File, 
        text='Ustawienia', 
        width=17, 
        bd=0, 
        bg=button_background, 
        fg=text, 
        relief='solid', 
        activebackground=button_activebackground, 
        activeforeground=text, 
        command=config_app)
add_json.pack(padx=10, pady=(10,2))


# query_board_game()

test.mainloop()