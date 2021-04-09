from telebot import types
from di_configuration import DIConfige, DIBot
from views import general


def studorganizations(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('ПРОФКОМ СТУДЕНТОВ')
    keyboard.add('МИИГАиК МЕДИА')
    keyboard.add('Спортивные секции')
    keyboard.add('Молодежный клуб РГО')
    keyboard.add('Меню')
    msg_org = bot.send_message(
        message.chat.id,
        'Перейдя по кнопке интересующей вас секции, можно узнать о ней подробнее',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg_org, org_info)


def org_info(message):
    bot = DIBot.di_bot()
    config = DIConfige.config_ini()
    if message.text == 'ПРОФКОМ СТУДЕНТОВ':
        keyboard = types.InlineKeyboardMarkup()
        web_button = types.InlineKeyboardButton(text="Сайт", url="https://mgugik.ru/")
        keyboard.add(web_button)
        msg_profkom = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["profkom"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_profkom, org_info)
    elif message.text == 'МИИГАиК МЕДИА':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/miigaikmedia")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/miigaik/")
        keyboard.add(vk_button, inst_button)
        msg_media = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["media"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_media, org_info)
    elif message.text == 'Спортивные секции':
        keyboard = types.InlineKeyboardMarkup()
        vk_btn = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/miigaik_sport")
        keyboard.add(vk_btn)
        msg_sport = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["sport"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_sport, org_info)
    elif message.text == 'Молодежный клуб РГО':
        keyboard = types.InlineKeyboardMarkup()
        vk_btn = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/mkrgo.miigaik")
        web_btn = types.InlineKeyboardButton(text="Сайт", url="https://mk.rgo.ru/")
        keyboard.add(vk_btn,web_btn)
        msg_rgo = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["rgo"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_rgo, org_info)
    elif message.text == 'Меню':
        general.help_message(message)
    else:
        msg_understand = bot.send_message(
            message.chat.id,
            'Я вас не понимаю, выберите раздел из меню')
        bot.register_next_step_handler(msg_understand, org_info)

handlers = {'studorganizations': studorganizations}