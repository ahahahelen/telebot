from telebot import types
from di_configuration import DIConfige, DIBot
from .open_menu import open_menu as menu


def openday(message):
    config = DIConfige.config_ini()
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Меню')
    open_d = bot.send_message(
        message.chat.id,
        'Приглашаем всех желающих (абитуриентов, школьников и их родителей) на День открытых дверей МИИГАиК.'
        ' Экскурсия по университету, презентации направлений подготовки, ответы на вопросы по'
        ' процессу обучения в вузе - все будет представлено на дне открытых дверей в Москве.\n\n'
        'Ближайший День открытых дверей в МИИГАиК состоится {} года по адресу:'
        ' Москва, Гороховский пер., 4. Проезд: ст. метро "Курская", выход к Гоголь-центру. \nНачало в 10:00\n'
        'Актуальную и подробную информацию Вы можете узнать на сайте '
        'http://www.miigaik.ru/ и в группе Вконтакте https://vk.com/miigaik'.format(config["OPENDAY"]["data"]),
        disable_web_page_preview=True,
        reply_markup=keyboard)
    bot.register_next_step_handler(open_d, open_menu)


def open_menu(message):
    menu(message)

handlers = {'openday': openday}