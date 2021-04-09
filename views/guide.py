from telebot import types
from di_configuration import DIBot
from .open_menu import open_menu as menu


def guide(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    keyboard.add('Список документов')
    keyboard.add('Меню')
    guide_msg = bot.send_message(
        message.chat.id,
        '<b>Чтобы поступить в МИИГАиК необходимо:\n'
        'Шаг 1:</b> До 25.07 подать заявление в МИИГАиК одним из способов:\n'
        '       1) В приемную коммисию, по адресу Москва, Гороховский пер., 4\n'
        '       <b>График работы:</b> по будням с 8.00 до 22.00, по субботам с 8.00 до 18.00\n'
        '       2) На почту pk@miigaik.ru\n\n'
        '<b>Шаг 2:</b> Следи за информацией на сайте:\n'
        'http://www.miigaik.ru/Abitur/competition/enrolled/\n\n'
        '<b>Шаг 3:</b> Принеси оригинал документов\n\n'
        '<b>Шаг 4:</b> Вы студент МИИГАиК!',
        parse_mode='HTML',
        reply_markup=keyboard)
    bot.register_next_step_handler(guide_msg, open_menu)


def open_menu(message):
    bot = DIBot.di_bot()
    if message.text == 'Меню':
        menu(message)
    elif message.text == 'Список документов':
        keyboard = types.InlineKeyboardMarkup()
        url_questionnaire = types.InlineKeyboardButton(
            text='Заявление о приеме',
            url='')
        url_statement = types.InlineKeyboardButton(
            text='Заявления о согласии на зачисление',
            url='')
        url_compliance = types.InlineKeyboardButton(
            text='',
            url='')
        keyboard.add(url_questionnaire)
        keyboard.add(url_statement)
        keyboard.add(url_compliance)
        bot.send_message(
            message.chat.id,
            'Поступающие в университет подают в приемную комиссию следующие документ\n'
            '1. <b>заявление</b> на имя ректора (заполняется на месте)\n'
            '2. 2 фотографии размером 3х4 см <b>(после зачисления)</b> для личного дела\n'
            '3. копию документа, удостоверяющего личность и гражданство; \n'
            '4. <b>согласие</b> на обработку персональных данных;\n'
            '5. <b>согласие на зачисление</b> по направлению.\n'
            '6. информацию о результатах единых государственных экзаменов\n'
            '7. документы, дающие право на льготы, установленные законодательством Российской Федерации\n'
            '8. документ (копия/оригинал), удостоверяющий образование соответствующего уровня\n',
            reply_markup=keyboard,
            parse_mode='HTML'
        )

handlers = {'guide': guide}

