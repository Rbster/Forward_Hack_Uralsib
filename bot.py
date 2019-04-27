# -*- coding: utf-8 -*-                                                                                                      
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-модуль почему-то просто telegram ¯\_(ツ)_/¯
from telegram.ext import CommandHandler  

def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте. Введите /help, чтобы посмотреть функционал данного бота.")

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Для Вас, у нас есть несколько команд, результаты которых, надеемся помогут Вам.\n1)/helpme - помогаем мы \n2)/support - по Вашему выбору скидываем в этот чат ссылку на телеграм канал (техподдержки) или телефон квалифицированного специалиста техподдержки")

def helpme(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Чем я могу Вам помочь?\n\n1)Подобрать для Вас подходящую услугу\n2)Связать Вас с техподдержкой.\nВведите только цифру!") 



updater = Updater(token='702809746:AAHmIm6mPpT1TLmkw1RqxsYF4SUfP2ebPqk')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует только на команду /start
helpme_handler = CommandHandler('helpme', helpme)  # этот обработчик реагирует только на команду /helpme
help_handler = CommandHandler('help', help)  # этот обработчик реагирует только на команду /help

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.dispatcher.add_handler(helpme_handler)   # регистрируем в госреестре обработчиков
updater.dispatcher.add_handler(help_handler)   # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!
