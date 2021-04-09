from telebot import types
from di_configuration import DIBot

def start_message(message):
    bot = DIBot.di_bot()
    print('start')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id,
        'Привет! Здесь собрана информация о Московском '
        'государственном университете геодеии и картографии',
        reply_markup=markup
    )
    help_message(message)


def help_message(message):
    bot = DIBot.di_bot()
    print('help')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id,
        'Я помогу тебе узнать немного больше о нашем ВУЗе\n'
        '/open_day - День открытых дверей\n'
        '/course - Курсы для абитуриентов\n'
        '/specialties - Направления подготовки\n'
        '/guide - Руководство по поступлению\n'
        '/contacts - Контактая информация\n'
        '/calculator - Калькулятор баллов\n'
        '/studorganizations - Внеучебная деятельность\n'
        '/map - Экскурсия по университету',
        reply_markup=markup
    )


handlers = {
    'start': start_message,
    'help': help_message
}
