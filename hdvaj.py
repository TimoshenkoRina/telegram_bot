import requests
from telebot import *

def pars(url): #функция парсит таблицу
    url = f'{url}'
    s = requests.Session()
    r = s.get(url, allow_redirects=True, timeout=10)
    r.encoding = 'utf-8'
    table = r.text.lower()
    return table

def english(table, chatid):
    lastname = users[chatid]['name']
    for a in table.split('\n'):
        if lastname in a:

            a = a[6:]
            a = a.split('"')
            s1 = float(a[0].count('1'))
            s2 = float(a[1].replace(',', '.'))
            s3 = float((a[4].split(',')[-2]).replace(',', '.'))
            return s1 + s2 + s3

    return 'ты не в этой группе'

def history(table, chatid):
    lastname = users[chatid]['name']
    for a in table.split('\n'):

        if lastname in a:
            a=a.split(',')
            return a[-2]

    return 'ты не в этой группе'

def irr(table, chatid):
    lastname = users[chatid]['name']
    for a in table.split('\n'):
        if lastname in a:
            sum = 0
            for item in a:
                if item and item.replace('.', '').replace('-', '').isdigit():
                    sum += int(item)

            return sum

    return 'ты не в этой группе'

def irs(table, chatid): #история современных международных отношений
    lastname = users[chatid]['name']
    table=table.replace('сул́има', 'сулима').replace('и́онова', 'ионова')

    for a in table.split('\n'):
        if lastname in a:

            a = [a for a in a.split(',') if a != 'н']

            return sum(int(a) for a in a[1:-1])

    return 'ты не в этой группе'

def org(table, chatid):
    lastname = users[chatid]['name']
    for a in table.split('\n'):

        if lastname in a:

            a = a[12:]
            a = a.split(',')
            return int(a[9]) + int(a[10])

    return 'ты не в этой группе'

def menedgment(table, chatid):
    lastname = users[chatid]['name']
    for a in table.split('\n'):

        if lastname in a:
            a = a.split('"')
            return a[-2]

    return 'ты не в этой группе'

url = [['ОРГ 1.2', 'https://docs.google.com/spreadsheets/d/1XQpCvLT5Nf-aQ8Mz-3VYDw0uyk-8QVKv98gLKSEQg9A/export?format=csv&id=1XQpCvLT5Nf-aQ8Mz-3VYDw0uyk-8QVKv98gLKSEQg9A&gid=0'],
       ['ОРГ 2.3', 'https://docs.google.com/spreadsheets/d/1DTkjRozRpijVK0Je9iZjLkpvbLAA-l6-WGnktJGlraU/export?format=csv&id=1DTkjRozRpijVK0Je9iZjLkpvbLAA-l6-WGnktJGlraU&gid=0'],
       ['ОРГ 2.1', 'https://docs.google.com/spreadsheets/d/1q9spgoTIUEbpwTqBuY5ml-Q5tSmDpuHTMx2QJnIZIBk/export?format=csv&id=1q9spgoTIUEbpwTqBuY5ml-Q5tSmDpuHTMx2QJnIZIBk&gid=0'],

       ['история россии и мира 8:10 Павловская','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=132554553'],
       ['история россии и мира 8:10 Пригодич','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=0'],
       ['история россии и мира 11:30 Пригодич','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=1821313907'],
       ['история россии и мира 15:30 Пригодич','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=605593543'],
       ['история россии и мира 9:50 Павловская','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=669992992'],
       ['история россии и мира 11:30 Павловская','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=517652382'],
       ['история россии и мира 13:30 Павловская','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=332322934'],
       ['история россии и мира 15:30 Павловская','https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=1487346128'],

       ['история современных международных отношений 3.1', 'https://docs.google.com/spreadsheets/d/1ZnR6uFz1t_uCdMLAMYRPaT8CpsQB8ALK/export?format=csv&id=1ZnR6uFz1t_uCdMLAMYRPaT8CpsQB8ALK&gid=1753157777'],
       ['история реформ и реформаторов 3.2', 'https://docs.google.com/spreadsheets/d/1AVP0_usl0u4d1VJ-W9dY83Z9XDXrfklK_OlxNc3oEbU/export?format=csv&id=1AVP0_usl0u4d1VJ-W9dY83Z9XDXrfklK_OlxNc3oEbU&gid=0'],

       ['менеджмент 1.1','https://docs.google.com/spreadsheets/d/1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms/export?format=csv&id=1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms&gid=0'],
       ['менеджмент 1.2','https://docs.google.com/spreadsheets/d/1BVhEkOZ7Yp7AuVSLIYAg9al3FVcBepVG76z2hDqm7Pg/export?format=csv&id=1BVhEkOZ7Yp7AuVSLIYAg9al3FVcBepVG76z2hDqm7Pg&gid=0'],
       ['менеджмент 1.3','https://docs.google.com/spreadsheets/d/1JS8C1dBMrIqDKV6Or_iaoSasA7wnG67xNs72nlGuXtE/export?format=csv&id=1JS8C1dBMrIqDKV6Or_iaoSasA7wnG67xNs72nlGuXtE&gid=0'],
       ['менеджмент 1.4','https://docs.google.com/spreadsheets/d/1RO9Z8TonVmE01S67zwRZbNY0TbeE21Z8ZXY5RQmn71c/export?format=csv&id=1RO9Z8TonVmE01S67zwRZbNY0TbeE21Z8ZXY5RQmn71c&gid=0'],
       ['менеджмент 1.5','https://docs.google.com/spreadsheets/d/1thf6a69OaRzbuxT76CQBgr1BGrQCq7OGy88ck3EBuaE/export?format=csv&id=1thf6a69OaRzbuxT76CQBgr1BGrQCq7OGy88ck3EBuaE&gid=0'],

       ['группа B12','https://docs.google.com/spreadsheets/d/1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w/export?format=csv&id=1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w&gid=474547065'],
       ['группа A2 d4','https://docs.google.com/spreadsheets/d/1XvdFQUgAZqOZ4onHpVUDGlw3jDKmhC_Gm7IV0cbPprE/export?format=csv&id=1XvdFQUgAZqOZ4onHpVUDGlw3jDKmhC_Gm7IV0cbPprE&gid=474547065']]

def z(predmet):
    for i in range(len(url)):
        if url[i][0]==predmet:
            return url[i][1]
    return predmet

bot = telebot.TeleBot('token')

bot.delete_webhook()

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
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    return markup

def cho_hosh():

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
        row_width=3,              # количество кнопок в строке
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

users = {}
answers = {
    "ОРГ": {
        "new": 0,
        "address": "ОРГ",
        "answer": "Теперь выберите поток ОРГ",
        "keyboard": "potokiORG",
        "start": "org"
    },
    "Основы менеджмента": {
        "new": 0,
        "address": "менеджмент",
        "answer": "Теперь выберите поток основ менеджмента",
        "keyboard": "potokimenegment",
        "start": "menegment"
    },
    "История": {
        "new": 0,
        "address": "история",
        "answer": "Теперь выберите раздел истории",
        "keyboard": "H_Types",
        "start": "history"
    },

    "орг 1.2": {
        "new": 2,
        "address": " 1.2",
        "answer": "Супер! вот ваши баллы:",
        "start": "org"
    },
    "орг 2.1": {
        "new": 2,
        "address": " 2.1",
        "answer": "Супер! вот ваши баллы:",
        "start": "org"
    },
    "орг 2.3": {
        "new": 2,
        "address": " 2.3",
        "answer": "Супер! вот ваши баллы:",
        "start": "org"
    },

    "ом 1.1": {
        "new": 2,
        "address": " 1.1",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.2": {
        "new": 2,
        "address": " 1.2",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.3": {
        "new": 2,
        "address": " 1.3",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.4": {
        "new": 2,
        "address": " 1.4",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.5": {
        "new": 2,
        "address": " 1.5",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },

    "России и мира": {
        "new": 1,
        "address": " россии и мира",
        "answer": "Теперь выберите время начала практики",
        "keyboard": "H_time",
        "start": "history"
    },
    "Реформы и реформаторы": {
        "new": 1,
        "address": " реформ и реформаторов",
        "answer": "Теперь выберите время начала практики",
        "keyboard": "H_time",
        "start": "history"
    },
    "Современные международные отношения": {
        "new": 1,
        "address": " современных международных отношений",
        "answer": "Теперь выберите поток",
        "keyboard": "IRS_Potok",
        "start": "irs"
    },

    "ирс 3.1": {
        "new": 2,
        "address": " 3.1",
        "answer": "Супер! вот ваши баллы:",
        "start": "irs"
    },

    "8:10":  {
        "new": 1,
        "address": " 8:10",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "9:50":  {
        "new": 1,
        "address": " 9:50",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "11:30":  {
        "new": 1,
        "address": " 11:30",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "13:30":  {
        "new": 1,
        "address": " 13:30",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "15:30":  {
        "new": 1,
        "address": " 15:30",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },

    "Павловская":  {
        "new": 2,
        "address": " Павловская",
        "answer": "Супер! вот ваши баллы:",
        "start": "history"
    },
    "Пригодич":  {
        "new": 2,
        "address": " Пригодич",
        "answer": "Супер! вот ваши баллы:",
        "start": "history"
    }
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    users[chat_id] = {}
    # Отправка сообщения с Reply-клавиатурой
    bot.send_message(message.chat.id,"Введите фамилию и имя через пробел", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_username)

def save_username(message):
    chat_id = message.chat.id
    name = message.text
    name = name.lower()
    name = name.strip()
    users[chat_id]['name'] = name
    bot.send_message(chat_id,"Выберите предмет по которому хотите узнать баллы", reply_markup=lessons())

# 5. Обработчик обычных кнопок
@bot.message_handler(content_types=['text'])
def handle_reply_buttons(message):
    if message.text == 'Выбрать предмет':
        bot.send_message(message.chat.id, "Выберите предмет по которому хотите узнать баллы", reply_markup=lessons())
        return
    if message.text == 'Пройти авторизацию заново':
        bot.send_message(message.chat.id, "Введите фамилию и имя через пробел", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, save_username)
        return

    if message.text not in answers:
        bot.send_message(message.chat.id, 'странные у тебя запросы какие-то, переделывай', reply_markup=cho_hosh())
        return

    if answers[message.text]['new'] == 0:
        users[message.chat.id]['fulladdress'] = answers[message.text]['address']
    elif answers[message.text]['new'] == 1:
        users[message.chat.id]['fulladdress'] += answers[message.text]['address']
    elif answers[message.text]['new'] == 2:
        users[message.chat.id]['fulladdress'] += answers[message.text]['address']

        if z(users[message.chat.id]['fulladdress']) == users[message.chat.id]['fulladdress']:
            bot.send_message(message.chat.id, 'Ты по моему перепутал, братанчик. Нет такой группы, иди лучше еще раз попробуй', reply_markup=cho_hosh())
            return

        if answers[message.text]['start'] == 'org':
            bot.send_message(message.chat.id, answers[message.text]['answer'] + f' {(org(pars(z(users[message.chat.id]['fulladdress'])), message.chat.id))}')
        elif answers[message.text]['start'] == 'menegment':
            bot.send_message(message.chat.id, answers[message.text]['answer'] + f' {(menedgment(pars(z(users[message.chat.id]['fulladdress'])), message.chat.id))}')
        elif answers[message.text]['start'] == 'history':
            bot.send_message(message.chat.id, answers[message.text]['answer'] + f' {(history(pars(z(users[message.chat.id]['fulladdress'])), message.chat.id))}')
        elif answers[message.text]['start'] == 'irs':
            bot.send_message(message.chat.id, answers[message.text]['answer'] + f' {(irs(pars(z(users[message.chat.id]['fulladdress'])), message.chat.id))}')
        bot.send_message(message.chat.id, 'Что дальше?', reply_markup=cho_hosh())
        return

    if answers[message.text]['keyboard'] == 'potokiORG':
        bot.send_message(message.chat.id, answers[message.text]['answer'], reply_markup=potokiORG())
    elif answers[message.text]['keyboard'] == 'potokimenegment':
        bot.send_message(message.chat.id, answers[message.text]['answer'], reply_markup=potokimenegment())
    elif answers[message.text]['keyboard'] == 'H_Types':
        bot.send_message(message.chat.id, answers[message.text]['answer'], reply_markup=H_Types())
    elif answers[message.text]['keyboard'] == 'H_time':
        bot.send_message(message.chat.id, answers[message.text]['answer'], reply_markup=H_time())
    elif answers[message.text]['keyboard'] == 'H_Teachers':
        bot.send_message(message.chat.id, answers[message.text]['answer'], reply_markup=H_Teachers())
    elif answers[message.text]['keyboard'] == 'IRS_Potok':
        bot.send_message(message.chat.id, answers[message.text]['answer'], reply_markup=IRS_Potok())

bot.polling()