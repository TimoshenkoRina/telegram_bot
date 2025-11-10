from telebot import *
from Bot_test.config import *
from Bot_test.pars import *
from Bot_test.keyboards import *

bot = TeleBot(TOKEN)
bot.delete_webhook()

users = {}

# авторизация по фамилии и имени
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    users[chat_id] = {}
    bot.send_message(chat_id, "Введите фамилию и имя через пробел", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, choose_org_flow)

# поток орг
def choose_org_flow(message):
    chat_id = message.chat.id
    fullname = message.text.lower().strip()
    users[chat_id]['name'] = fullname

    bot.send_message(chat_id, "Выберите поток по ОРГ:", reply_markup=potokiORG())
    bot.register_next_step_handler(message, process_org_flow)

def process_org_flow(message):
    chat_id = message.chat.id
    flow = message.text.lower()

    # Формируем полный адрес по орг
    fulladdress = 'орг ' + flow
    users[chat_id]['org_fulladdress'] = fulladdress

    # Проверяем что пользователь есть в потоке
    url_org = get_url(fulladdress)
    if url_org is None:
        bot.send_message(chat_id, "Поток не найден! Попробуйте снова.", reply_markup=potokiORG())
        bot.register_next_step_handler(message, process_org_flow)
        return

    raw_data = pars(url_org)
    score = org(raw_data, chat_id, users)
    if score == 'ты не в этой группе':
        bot.send_message(chat_id, "Вас нет в этом потоке ОРГ, выберите другой.", reply_markup=potokiORG())
        bot.register_next_step_handler(message, process_org_flow)
        return
    users[chat_id]['org_score'] = score

    # вызываем функцию для английского
    choose_english_flow(message)

# поток английского
def choose_english_flow(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Выберите поток по английскому:", reply_markup=E_level())
    bot.register_next_step_handler(message, process_english_flow)

def process_english_flow(message):
    chat_id = message.chat.id
    flow = message.text.lower()

    fulladdress = 'английский ' + flow
    users[chat_id]['english_fulladdress'] = fulladdress

    url_english = get_url(fulladdress)
    if url_english is None:
        bot.send_message(chat_id, "Поток не найден! Попробуйте снова.", reply_markup=E_level())
        bot.register_next_step_handler(message, process_english_flow)
        return

    raw_data = pars(url_english)
    score = english(raw_data, chat_id, users)
    if score == 'ты не в этой группе':
        bot.send_message(chat_id, "Вас нет в этом потоке английского, выберите другой.", reply_markup=E_level())
        bot.register_next_step_handler(message, process_english_flow)
        return
    users[chat_id]['english_score'] = score

    # вызываем функцию для менеджмента
    choose_management_flow(message)

# поток менеджмента
def choose_management_flow(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Выберите поток по менеджменту:", reply_markup=potokimenegment())
    bot.register_next_step_handler(message, process_management_flow)

def process_management_flow(message):
    chat_id = message.chat.id
    flow = message.text.lower()

    fulladdress = 'менеджмент ' + flow
    users[chat_id]['menegment_fulladdress'] = fulladdress

    url_menegment = get_url(fulladdress)
    if url_menegment is None:
        bot.send_message(chat_id, "Поток не найден! Попробуйте снова.", reply_markup=potokimenegment())
        bot.register_next_step_handler(message, process_management_flow)
        return

    raw_data = pars(url_menegment)
    score = menedgment(raw_data, chat_id, users)
    if score == 'ты не в этой группе':
        bot.send_message(chat_id, "Вас нет в этом потоке менеджмента, выберите другой.", reply_markup=potokimenegment())
        bot.register_next_step_handler(message, process_management_flow)
        return
    users[chat_id]['menegment_score'] = score

    # Переходим к выбору потока истории
    choose_history_flow(message)

# поток истории
def choose_history_flow(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Выберите поток по истории:", reply_markup=H_Types())
    bot.register_next_step_handler(message, process_history_flow)

def process_history_flow(message):
    chat_id = message.chat.id
    flow = message.text.lower()
    # разделяем потоки истории для конкретной функции
    if 'россии' in flow:
        fulladdress = 'история ' + flow
        get_score_func = history
    elif 'современные' in flow:
        fulladdress = 'история ' + flow
        get_score_func = irs
    elif 'реформ' in flow:
        fulladdress = 'история ' + flow
        get_score_func = irr
    else:
        bot.send_message(chat_id, "Поток истории не распознан. Попробуйте снова.", reply_markup=H_Types())
        bot.register_next_step_handler(message, process_history_flow)
        return

    users[chat_id]['history_fulladdress'] = fulladdress

    url_history = get_url(fulladdress)
    if url_history is None:
        bot.send_message(chat_id, "Поток не найден! Попробуйте снова.", reply_markup=H_Types())
        bot.register_next_step_handler(message, process_history_flow)
        return

    raw_data = pars(url_history)
    score = get_score_func(raw_data, chat_id, users)
    if score == 'ты не в этой группе':
        bot.send_message(chat_id, "Вас нет в этом потоке истории, выберите другой.", reply_markup=H_Types())
        bot.register_next_step_handler(message, process_history_flow)
        return
    users[chat_id]['history_score'] = score


    send_all_scores(chat_id)

def send_all_scores(chat_id):

    result = (
        f"Вот ваши баллы по всем предметам:\n"
        f"История: {users[chat_id].get('history_score')}\n"
        f"ОРГ: {users[chat_id].get('org_score')}\n"
        f"Менеджмент: {users[chat_id].get('menegment_score')}\n"
        f"Английский: {users[chat_id].get('english_score')}\n"
    )
    bot.send_message(chat_id, result)
    bot.send_message(chat_id, "Спасибо, что пользуетесь ботом! Чтобы начать заново, введите /start.")

bot.polling()
