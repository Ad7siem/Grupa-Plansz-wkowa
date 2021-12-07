from tkinter import *
from sheet import OpenSheet

# Create function to Detelete Board Games
def delete_board_game():
    global w_dBG
    w_dBG = Tk()
    w_dBG.title('Usuwanie planszówki')
    w_dBG.geometry('320x80')

    global delete_box
    delete_box = Entry(w_dBG, width=10)
    delete_box.grid(row=0, column=1, padx=20)

    delete_box_label = Label(w_dBG, text='Id planszówki do usunięcia:')
    delete_box_label.grid(row=0, column=0, padx=20)

    delete_button = Button(w_dBG, text='Usuń planszówkę', command=delete)
    delete_button.grid(row=1, column=0, columnspan=2, pady=10)


# Create Function in Delete Button
def delete():

    worksheet = OpenSheet()

    position = int(delete_box.get())
    length = len(worksheet.get_all_values())

    worksheet.delete_rows(int(delete_box.get()) + 1)
    while position + 1 <= length - 1:
        worksheet.update_cell(position + 1, 1 ,position)
        position += 1

    w_dBG.destroy()