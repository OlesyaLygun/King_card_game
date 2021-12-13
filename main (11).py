import Phrases
import tkinter
import Binary_tree

window_width = 800
window_height = 600
card_parameters = [250, 100, 550, 500]
current_number = 1
questions = []
Yes_responce = []
No_responce = []


class Player():

    def __init__(self):
        self.reputation = 10
        self.money = 20
        self.is_Dead = False


def cleaning():
    ordinary_page.create_rectangle(0, 0, window_width, window_height,
                                   fill='aquamarine')
    ordinary_page.create_rectangle(card_parameters[0], card_parameters[1], card_parameters[2], card_parameters[3],
                                   fill='white', width='2')
    ordinary_page.create_text(window_width * 0.85, window_height * 5 / 6,
                              text=('Ваша репутация:' + str(King.reputation)), justify=tkinter.CENTER,
                              font=('Helvetica', '9', 'italic'))
    ordinary_page.create_text(window_width * 0.85, window_height * 8 / 9,
                              text=('Ваши деньги:' + str(King.money)), justify=tkinter.CENTER,
                              font=('Helvetica', '9', 'italic'))


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
    if King.is_Dead != True:
        global current_number
        if Yes_or_No == "Yes":
            cleaning()
            if (Phrases.CheckDeath(Yes_responce[number * 2 - 1]) != 'False'):
                King.is_Dead = True
            printing(Yes_responce[number * 2 - 2] + '\n' + 'Репутация: ' + Yes_responce[number * 2 - 1].split(', ')[1] +
                     ', деньги: ' + Yes_responce[number * 2 - 1].split(', ')[0])
            King.money += int(Yes_responce[number * 2 - 1].split(', ')[0])
            King.reputation += int(Yes_responce[number*2 - 1].split(', ')[1])
        if Yes_or_No == "No":
            cleaning()
            if (Phrases.CheckDeath(No_responce[number * 2 - 1]) != 'False'):
                King.is_Dead = True
            printing(No_responce[number * 2 - 2] + '\n' + 'Репутация: ' + No_responce[number * 2 - 1].split(', ')[1] +
                     ', деньги: ' + No_responce[number * 2 - 1].split(', ')[0])
            King.money += int(No_responce[number * 2 - 1].split(', ')[0])
            King.reputation += int(No_responce[number * 2 - 1].split(', ')[1])

        if King.money <= 0 or King.reputation <= 0:
            King.is_Dead = True
        if King.is_Dead != True:
            ordinary_page.update()
            current_number += 1
            ordinary_page.after(3000, cleaning())
            printing(questions[number])
            ordinary_page.create_text(card_parameters[0] + (card_parameters[2] - card_parameters[0]) / 2,
                                      150,
                                      text=('Карточка ' + str(current_number)), justify=tkinter.CENTER,
                                      font=('Helvetica', '15', 'italic'))
        else:
            ordinary_page.update()
            cleaning()
            ordinary_page.after(1500, cleaning())
            printing("Вы умерли! Поздравляю")
    else:
        cleaning()
        printing("Вы умерли! Поздравляю")



def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global ordinary_page, No_button
    root = tkinter.Tk()
    ordinary_page = tkinter.Canvas(root, width=window_width, height=window_height, bg="aquamarine")
    Phrases.ReadReact('yes.txt', 'yesnum.txt', Yes_responce)
    Phrases.ReadReact('Нет.txt', 'НетРез.txt', No_responce)
    Phrases.ReadQuest('Утверждения.txt', questions)

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
    printing(questions[0])
    ordinary_page.create_text(card_parameters[0] + (card_parameters[2] - card_parameters[0]) / 2,
                              150,
                              text=('Карточка ' + str(current_number // 2 + 1)), justify=tkinter.CENTER,
                              font=('Helvetica', '15', 'italic'))

    root.mainloop()


if __name__ == "__main__":
    main()