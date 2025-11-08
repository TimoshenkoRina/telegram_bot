from config import TOKEN, answers
from pars import pars, english, history, irr, irs, org, menedgment, get_url
from keyboards import (
    lessons, restart, potokiORG, potokimenegment, H_Types, H_time, H_Teachers,
    IRS_Potok, E_level, E_B12_groups, E_A2_groups, IRR_Potok
)
from telebot import types, TeleBot

bot = TeleBot(TOKEN)
bot.delete_webhook()

users = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    users[chat_id] = {}
    bot.send_message(chat_id, "Введите фамилию и имя через пробел", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_username)

def save_username(message):
    chat_id = message.chat.id
    name = message.text.lower().strip()
    users[chat_id]['name'] = name
    bot.send_message(chat_id, "Выберите предмет по которому хотите узнать баллы", reply_markup=lessons())

@bot.message_handler(content_types=['text'])
def handle_reply_buttons(message):
    chat_id = message.chat.id
    text = message.text

    if text == 'Пройти авторизацию заново':
        bot.send_message(chat_id, "Введите фамилию и имя через пробел", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, save_username)  # следующий ввод обработает save_username
        return

    if text == 'Выбрать предмет':
        bot.send_message(chat_id, "Выберите предмет по которому хотите узнать баллы", reply_markup=lessons())
        return

    if text not in answers:
        bot.send_message(chat_id, 'Странный запрос, переделывай', reply_markup=restart())
        return

    if answers[message.text]['new'] == 0:
        users[message.chat.id]['fulladdress'] = answers[message.text]['address']
    elif answers[message.text]['new'] == 1:
        users[message.chat.id]['fulladdress'] += answers[message.text]['address']
    elif answers[message.text]['new'] == 2:
        users[message.chat.id]['fulladdress'] += answers[message.text]['address']

    fulladdress = users[chat_id]['fulladdress']

    # когда выбрана конкретная группа
    if answers[text]['new'] == 2:
        url = get_url(fulladdress)
        if url == fulladdress:
            bot.send_message(chat_id, 'Ты по-моему перепутал, братанчик. Нет такой группы, попробуй ещё раз', reply_markup=restart())
            return

        # сознаём ключи и кидаем в функцию с обработкой таблицы
        func_map = {
            'org': org,
            'menegment': menedgment,
            'history': history,
            'irs': irs,
            'english': english,
            'irr': irr
        }

        func = func_map.get(answers[text]['start'])

        if func:
            raw_data = pars(url)  # парсим таблицу
            ans = func(raw_data, chat_id, users)  # передаём данные пользователя
        else:
            ans = 'Неизвестная категория'

        if ans == 'ты не в этой группе':
            bot.send_message(chat_id, ans)
        else:
            bot.send_message(chat_id, f"Супер! вот ваши баллы: {ans}")


        bot.send_message(chat_id, 'Что дальше?', reply_markup=restart())
        return

    keyb_map = {
        'potokiORG': potokiORG,
        'potokimenegment': potokimenegment,
        'H_Types': H_Types,
        'H_time': H_time,
        'H_Teachers': H_Teachers,
        'IRS_Potok': IRS_Potok,
        'E_level': E_level,
        'E_B12_groups': E_B12_groups,
        'E_A2_groups': E_A2_groups,
        'IRR_Potok': IRR_Potok
    }

    keyboard_func = keyb_map.get(answers[text].get('keyboard'))
    if keyboard_func:
        bot.send_message(chat_id, answers[text]['answer'], reply_markup=keyboard_func())

bot.polling(none_stop=True)
