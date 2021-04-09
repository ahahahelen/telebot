from telebot import types
from views import general
from di_configuration import DIConfige, DIBot

def course(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Архитектурно-художественная школа МИИГАиК')
    keyboard.row('Подготовка к ЕГЭ и внутренним экзаменам')
    keyboard.row('Меню')
    msg = bot.send_message(message.chat.id, 'Выбери интересующий курс', reply_markup=keyboard)
    bot.register_next_step_handler(msg,course_info)


def course_info(message):
    config = DIConfige.config_ini()
    bot = DIBot.di_bot()
    if message.text == 'Подготовка к ЕГЭ и внутренним экзаменам':
        bot.send_message(message.chat.id, text=config["COURSE"]["ege"], parse_mode='HTML')
        msg_exam = bot.send_message(message.chat.id, 'Получить более подробную информацию, а также записаться на курсы,'
                                                     ' можно перейдя по ссылке: http://www.miigaik.ru/applicants/courses/college/',
                                    disable_web_page_preview=True)
        bot.register_next_step_handler(msg_exam, course_info)
    elif message.text == 'Архитектурно-художественная школа МИИГАиК':
        bot.send_message(message.chat.id, '<b>Архитектурно-художественная школа МИИГАиК</b>\n'
                                          'Архитектурно-художественная школа (АХШ) - это подготовительные курсы, направленные на подготовку к сдаче вступительных экзаменов и к дальнейшему обучению на кафедре «Архитектуры и ландшафта» в МИИГАиК.'
                                          'Обучение в АХШ происходит по трём направлениям:\n'
                                          ' 1.Черчение\n'
                                          '2.Рисунок светотеневой (натюрморт)\n'
                                          '3.Рисунок линейно-конструктивный (композиция)\n'
                                          'Срок обучения в школе – от 1 до 3 лет.\n'
                                          'Занятия проводятся 3 раза в неделю ведущими преподавателями кафедры архитектуры и ландшафта, кафедры архитектурного проектирования.\n', parse_mode='HTML')
        msg_school = bot.send_message(message.chat.id, 'Получить более подробную информацию можно перейдя по ссылке: '
                                                       'http://www.miigaik.ru/archschool//',
                                      disable_web_page_preview=True, parse_mode='HTML')
        bot.register_next_step_handler(msg_school, course_info)
    elif message.text == 'Меню':
        general.help_message(message)
    else:
        try:
            if message.text == 'Меню':
                general.help_message(message)
        except:
            print('ERROR')

handlers = {'course': course}