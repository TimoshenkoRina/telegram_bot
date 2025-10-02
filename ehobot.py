#!/usr/bin/python

import asyncio #импортируем библиотеку, которая позволяет использовать ассинхронное программирование

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot ('8325763973:AAFOr4FwgtZTrXATle2tkqYBms_W7WAASNo') #записываем токен бота

@bot.message_handler(commands=['start', 'help']) #добавляем в бот команды, на которые он пока не отвечает

async def send_welcome(message):
    text = 'HI'
    await bot.reply_to(message, text)
    #       await и async перед функцией так же используются для ассинхронки,
    #       чтобы бот мог обрабатывать несколько запросов одновременно

@bot.message_handler(func=lambda message: True)

async def echo(message):
    await bot.reply_to(message, message.text)

asyncio.run(bot.polling()) #запускает бот


















