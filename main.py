import tkinter

import Phrases
from Phrases import *

window_width = 800
window_height = 600
card_parameters = [250, 100, 550, 500]
current_number = 0


class Player():

    def __init__(self):
        self.reputation = 50
        self.money = 100


def cleaning():
    ordinary_page.create_rectangle(card_parameters[0], card_parameters[1], card_parameters[2], card_parameters[3],
                                   fill='white', width='2')

King = Player()

def printing(text, number=-3):
    temporary = text.split()
    len_of_str = 0
    for i in temporary:
        len_of_str += (len(i) + 1) * 10
        if len_of_str >= card_parameters[2] - card_parameters[0]:
            len_of_str = 0
            temporary.insert(temporary.index(i), '\n')
    text = ' '.join(temporary)
    id = ordinary_page.create_text(card_parameters[0] + (card_parameters[2] - card_parameters[0]) / 2,
                                   card_parameters[1] + (card_parameters[3] - card_parameters[1]) / 2,
                                   text=text, justify=tkinter.CENTER)


def response(Yes_or_No, number):
    global current_number
    if Yes_or_No == "Yes":
        cleaning()
        printing(Phrases.Yes_responce[number])
        King.money += int(Phrases.Yes_responce[number + 1].split(', ')[0])
        King.reputation += int(Phrases.Yes_responce[number + 1].split(', ')[1])
    if Yes_or_No == "No":
        cleaning()
        printing(Phrases.No_responce[number])
        King.money += int(Phrases.No_responce[number + 1].split(', ')[0])
        King.reputation += int(Phrases.No_responce[number + 1].split(', ')[1])

    print(King.money, King.reputation)
    ordinary_page.update()
    current_number += 2
    ordinary_page.after(1500, cleaning())
    printing(questions[number + 2])
    ordinary_page.create_text(card_parameters[0] + (card_parameters[2] - card_parameters[0]) / 2,
                              150,
                              text=('Карточка ' + str(current_number)), justify=tkinter.CENTER,
                              font=('Helvetica', '15', 'italic'))


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global ordinary_page
    root = tkinter.Tk()
    ordinary_page = tkinter.Canvas(root, width=window_width, height=window_height, bg="aquamarine")

    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)
    ordinary_page.pack(side=tkinter.TOP)
    Yes_button = tkinter.Button(frame, text="Yes!", command=lambda: response("Yes", current_number), width=6)
    Yes_button.pack(side=tkinter.LEFT)
    GoF_button = tkinter.Button(frame, text="Get lost", command=lambda: print("Get lost"))
    GoF_button.pack(side=tkinter.LEFT)
    No_button = tkinter.Button(frame, text="No!", command=lambda: response("No", current_number), width=6)
    No_button.pack(side=tkinter.LEFT)

    cleaning()
    printing(Phrases.questions[0])
    ordinary_page.create_text(card_parameters[0] + (card_parameters[2] - card_parameters[0]) / 2,
                              150,
                              text=('Карточка ' + str(current_number // 2 + 1)), justify=tkinter.CENTER,
                              font=('Helvetica', '15', 'italic'))
    root.mainloop()


if __name__ == "__main__":
    main()
