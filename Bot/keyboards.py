from telebot import types

def lessons():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=3,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    start_button = types.KeyboardButton("start")
    btn1 = types.KeyboardButton("ОРГ")
    btn2 = types.KeyboardButton("Основы менеджмента")
    btn3 = types.KeyboardButton("История")
    btn4 = types.KeyboardButton("Английский язык")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup

def restart():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=2,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("Выбрать предмет")
    btn2 = types.InlineKeyboardButton("Пройти авторизацию заново")
    markup.add(btn1)
    markup.add(btn2)
    return markup

def H_Types():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=4,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("России и мира")
    btn2 = types.KeyboardButton("Реформы и реформаторы")
    btn3 = types.KeyboardButton("Современные международные отношения")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    return markup

def IRS_Potok():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=1,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("ирс 3.1")
    markup.add(btn1)
    return markup

def IRR_Potok():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=1,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("ирр 3.2")
    markup.add(btn1)
    return markup

def H_Teachers():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=2,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("Павловская")
    btn2 = types.KeyboardButton("Пригодич")
    markup.add(btn1)
    markup.add(btn2)
    return markup

def H_time():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=5,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("8:10")
    btn2 = types.KeyboardButton("9:50")
    btn3 = types.KeyboardButton("11:30")
    btn4 = types.KeyboardButton("13:30")
    btn5 = types.KeyboardButton("15:30")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    return markup

def E_level():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=2,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("B1.2")
    btn2 = types.KeyboardButton("A2")
    markup.add(btn1)
    markup.add(btn2)
    return markup

def E_B12_groups():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=1,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("B1.2 7")
    markup.add(btn1)
    return markup

def E_A2_groups():

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,      # автоматическое изменение размера
        row_width=1,              # количество кнопок в строке
        one_time_keyboard=True    # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("A2 d4")
    markup.add(btn1)
    return markup

def potokiORG():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,  # автоматическое изменение размера
        row_width=3,  # количество кнопок в строке
        one_time_keyboard=True  # скрыть после использования
    )
    markup = types.ReplyKeyboardMarkup(row_width=3)
    potok12 = types.KeyboardButton("орг 1.2")
    potok21 = types.KeyboardButton("орг 2.1")
    potok23 = types.KeyboardButton("орг 2.3")
    markup.add(potok12)
    markup.add(potok21)
    markup.add(potok23)
    return markup

def potokimenegment():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,  # автоматическое изменение размера
        row_width=5,  # количество кнопок в строке
        one_time_keyboard=True  # скрыть после использования
    )

    markup = types.ReplyKeyboardMarkup(row_width=3)
    potok11 = types.KeyboardButton("ом 1.1")
    potok12 = types.KeyboardButton("ом 1.2")
    potok13 = types.KeyboardButton("ом 1.3")
    potok14 = types.KeyboardButton("ом 1.4")
    potok15 = types.KeyboardButton("ом 1.5")
    markup.add(potok11)
    markup.add(potok12)
    markup.add(potok13)
    markup.add(potok14)
    markup.add(potok15)
    return markup