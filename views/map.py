from telebot import types
from di_configuration import DIBot

def map(message):
    print('map')
    bot = DIBot.di_bot()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text='Карта МИИГАиК',
        url='http://map.miigaik.ru/')
    keyboard.add(url_button)
    bot.send_photo(
        message.from_user.id,
            photo='',
        reply_markup=keyboard)

handlers = {'map': map}