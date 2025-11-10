from telebot import types

def lessons():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=3,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("ОРГ")
    btn2 = types.KeyboardButton("Основы менеджмента")
    btn3 = types.KeyboardButton("История")
    btn4 = types.KeyboardButton("Английский язык")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def restart():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("Выбрать предмет")
    btn2 = types.KeyboardButton("Пройти авторизацию заново")
    markup.add(btn1, btn2)
    return markup

def H_Types():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=3,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("России и мира")
    btn2 = types.KeyboardButton("Реформы и реформаторы")
    btn3 = types.KeyboardButton("Современные международные отношения")
    markup.add(btn1, btn2, btn3)
    return markup

def IRS_Potok():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("ирс 3.1")
    markup.add(btn1)
    return markup

def IRR_Potok():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("ирр 3.2")
    markup.add(btn1)
    return markup

def E_level():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("B1.2 7")
    btn2 = types.KeyboardButton("A2")
    markup.add(btn1, btn2)
    return markup

def E_B12_groups():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("B1.2 7")
    markup.add(btn1)
    return markup

def E_A2_groups():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
        one_time_keyboard=True
    )
    btn1 = types.KeyboardButton("A2 d4")
    markup.add(btn1)
    return markup

def potokiORG():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=3,
        one_time_keyboard=True
    )
    potok12 = types.KeyboardButton(" 1.2")
    potok21 = types.KeyboardButton(" 2.1")
    potok23 = types.KeyboardButton(" 2.3")
    markup.add(potok12, potok21, potok23)
    return markup

def potokimenegment():
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=5,
        one_time_keyboard=True
    )
    potok11 = types.KeyboardButton("1.1")
    potok12 = types.KeyboardButton("1.2")
    potok13 = types.KeyboardButton("1.3")
    potok14 = types.KeyboardButton("1.4")
    potok15 = types.KeyboardButton("1.5")
    markup.add(potok11, potok12, potok13, potok14, potok15)
    return markup
