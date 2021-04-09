from telebot import types
from di_configuration import DIBot
from .open_menu import open_menu as menu

def contacts(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Меню')
    bot.send_message(
        message.chat.id,
        text='<b>Контактная информация</b>\n\n'
             '<b>Телефон приемной комиссии: 8 (499) 267-15-45 (Москва)\n'
             '<b>Email:</b> portal@miigaik.ru\n'
             '<b>Режим работы: по будням с 8.00 до 22.00, по субботам с 8.00 до 18.00\n'
             'Проезд: ст. метро "Курская", выход к Гоголь-центру',
        parse_mode='HTML')
    contact_msg = bot.send_venue(
        message.chat.id,
        55.763488, 37.662039,
        'Адрес:',
        '105064, Москва, Гороховский пер., 4',
        reply_markup=keyboard)
    bot.register_next_step_handler(contact_msg, open_menu)

def open_menu(message):
    menu(message)

handlers = {'contacts': contacts}