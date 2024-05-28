score = 0


def location_1():
    global score
    print("Локация 1: Лошадка стоит и щиплет травку")
    print("Что вы хотите сделать?")
    print("1. Начать идти")
    print("2. Остановиться")
    print("3. Отдыхать")

    choice = input("Выберите действие: ")
    if choice == "1":
        transition_start()
        score = 10
    elif choice == "2":
        location_1()
    elif choice == "3":
        rest()
        score = 5
    else:
        print("Неправильный выбор. Попробуйте ещё раз.")
        location_1()


def location_2():
    global score
    print("Локация 2: Лошадка без устали идёт в сторону своего пастбища")
    print("Что вы хотите сделать?")
    print("1. Продолжить идти")
    print("2. Остановиться")

    choice = input("Выберите действие: ")
    if choice == "1":
        transition_continue()
        score = 10
    elif choice == "2":
        location_1()
    else:
        print("Неправильный выбор. Попробуйте ещё раз.")
        location_2()


def location_3():
    global score
    print("Локация 3: Лошадка приближается к своему пастбищу")
    print("Что вы хотите сделать?")
    print("1. Пойти к пастбищу")
    print("2. Остановиться")

    choice = input("Выберите действие: ")
    if choice == "1":
        pasture()
        score = 20
    elif choice == "2":
        location_2()
    else:
        print("Неправильный выбор. Попробуйте ещё раз.")
        location_3()


def transition_start():
    global score
    print("Начать идти: Лошадка встала и отряхнула голову от налетевших мух.")
    print("Сначала она сделала неуверенный шаг, потом второй.")
    print("И вот Лошадка уже идёт в сторону своего пастбища.")
    input("Нажмите Enter для продолжения...")
    location_2()


def transition_continue():
    global score
    location_3()


def rest():
    global score
    print("Отдыхать: Лошадка расслабилась и начала жевать травку.")
    input("Нажмите Enter для продолжения...")
    location_1()


def pasture():
    global score
    print("Пастбище: Лошадка наконец-то достигла своего пастбища и начала пастись.")
    print("История завершена. Спасибо за игру!")
    print("Ваш счет:", score)
    qw = input("Начать игру заного?")
    if qw == 'да' or 'Да':
        location_1()
    else:
        print("Хорошего дня, игра закончилась!")
        exit()

if __name__ =='__main__':
    location_1()
