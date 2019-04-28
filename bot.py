# -*- coding: utf-8 -*-                                                                                                      
# пакет называется python-telegram-bot, но Python-модуль почему-то просто telegram ¯\_(ツ)_/¯

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler,\
                         RegexHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)




def start(bot, update):
    msg = 'Здравствуйте, Вы обратились к боту помощнику банка Уралсиб \nДля помощи выберите команду /help \nНо вначала расскажите, где вы находитесь? \nТак мы сможем понять, как вам помочь :)'

    reply_kb_markup = telegram.ReplyKeyboardMarkup([
                                                    [telegram.KeyboardButton('Поделиться геопозицией', 
                                                                             request_location=True)]
                                                    ],
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
   # print(update.user_id)

    bot.sendMessage(chat_id=update.message.chat_id,
                    text=msg, 
                    reply_markup=reply_kb_markup)


def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Для Вас, у нас есть несколько команд, результаты которых, надеемся помогут Вам.\n1)/helpme - помогаем мы \n2)/support - по Вашему выбору скидываем в этот чат ссылку на телеграм канал (техподдержки) или телефон квалифицированного специалиста техподдержки")

def support(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Как Вы хотите связаться с техподдержкой? Есть два варианта:\n1)/number - прислать Вам номер телефона специалиста\n2)/link - скидываем сюда ссылку на телеграм канал техподдержки\n!")

def link(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="ссылка:<ссылка>")
    
def number(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="88002505757")
    
def helpme(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Чем я могу Вам помочь?\n\n1)Подобрать для Вас подходящую услугу\n2)Связать Вас с техподдержкой.\nВведите просто цифру как команду(например:/1)!") 

def two(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="<ссылка>")
    
def one(bot,update):
    msg="Какое Вы лицо:Физическое или юридическое?"
    kb_markup = telegram.ReplyKeyboardMarkup([
                                                    [telegram.KeyboardButton('Физическое', 
                                                                             reply_msg='Физическое')],
                                                    [telegram.KeyboardButton('Юридическое', 
                                                                             reply_msg='Юридическое')]
                                                    ],
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

   # print(update.user_id)

    bot.sendMessage(chat_id=update.message.chat_id,
                    text=msg, 
                    reply_markup=kb_markup)
def yuri(bot, update):
    kb_markup = telegram.ReplyKeyboardMarkup([
                                                    [telegram.KeyboardButton('Заплатить за Интернет', 
                                                                             reply_msg='Заплатить за Интернет')],
                                                    [telegram.KeyboardButton('Заплатить за коммуналку', 
                                                                             reply_msg='Заплатить за коммуналку')],
                                                    [telegram.KeyboardButton('Заплатить за ТВ', 
                                                                             reply_msg='Заплатить за ТВ')],
                                                    [telegram.KeyboardButton('Заплатить за телефон', 
                                                                             reply_msg='Заплатить за телефон')],
                                                    [telegram.KeyboardButton('Заплатить за образование', 
                                                                             reply_msg='Заплатить за образование')],
                                                    [telegram.KeyboardButton('Заплатить за систему безопасности', 
                                                                             reply_msg='Заплатить за систему безопасности')],
                                                    ],
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
   # print(update.user_id)

    bot.sendMessage(chat_id=update.message.chat_id,
                    text=msg, 
                    reply_markup=kb_markup)

def fiz(bot, update):
    kb_markup = telegram.ReplyKeyboardMarkup([
                                                    [telegram.KeyboardButton('Заплатить за Интернет', 
                                                                             reply_msg='Заплатить за Интернет')],
                                                    [telegram.KeyboardButton('Заплатить за коммуналку', 
                                                                             reply_msg='Заплатить за коммуналку')],
                                                    [telegram.KeyboardButton('Заплатить за ТВ', 
                                                                             reply_msg='Заплатить за ТВ')],
                                                    [telegram.KeyboardButton('Заплатить за телефон', 
                                                                             reply_msg='Заплатить за телефон')],
                                                    [telegram.KeyboardButton('Получить кредит', 
                                                                             reply_msg='Получить кредит')],
                                                    [telegram.KeyboardButton('Пополнить счет', 
                                                                             reply_msg='Пополнить счет')],
                                                    ],
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
   # print(update.user_id)

    bot.sendMessage(chat_id=update.message.chat_id,
                    text=msg, 
                    reply_markup=kb_markup)


# def get_location(bot, update):
#     target_latitude = update.message.location.latitude
#     target_longitude = update.message.location.longitude
#     bot.sendMessage(chat_id=update.message.chat_id, text="Ваши координаты:" + target_latitude + ' ' + target_longitude)
'''
def callbackHandler(bot,update):
    query = update.callback_query
    username = update.effective_user.username
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    if int(query.data) == 1:
        bot.sendPhoto(photo=getcat(),
                      chat_id=chat_id,
                      message_id=message_id,
                      reply_markup=draw_button())
'''

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


updater = Updater(token='702809746:AAHmIm6mPpT1TLmkw1RqxsYF4SUfP2ebPqk')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует только на команду /start
helpme_handler = CommandHandler('helpme', helpme)  # этот обработчик реагирует только на команду /helpme
help_handler = CommandHandler('help', help)  # этот обработчик реагирует только на команду /help
two_handler = CommandHandler('2', two)
support_handler = CommandHandler('support', support)
link_handler = CommandHandler('link', link)
number_handler = CommandHandler('number', number)
one_handler = CommandHandler('1', one)
yuri_handler = CommandHandler('Юридическое', yuri)
fiz_handler = CommandHandler('Юридическое', fiz)





dp = updater.dispatcher
dp.add_handler(start_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(helpme_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(help_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(two_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(support_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(link_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(number_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(one_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(yuri_handler)   # регистрируем в госреестре обработчиков
dp.add_handler(fiz_handler)   # регистрируем в госреестре обработчиков

###dp.add_handler(CallbackQueryHandler(callbackHandler, pass_chat_data=True))


dp.add_error_handler(error)

updater.start_polling()  # поехали!

updater.idle()
