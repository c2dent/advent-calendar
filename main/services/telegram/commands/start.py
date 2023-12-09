from django.conf import settings
from telebot import types, TeleBot
from telebot.types import MenuButtonWebApp, WebAppInfo

from main.services.tg_user_service import TgUserService


def start(m: types.Message, bot: TeleBot):
    message = "<strong>Давайте начнем!🎄</strong> \nЧтобы начать, нажмите кнопку ниже."

    url = "https://" + settings.MAIN_HOST + "/advent/" + str(m.chat.id) + "/"
    TgUserService.get_or_create(m)

    reply_markup = types.InlineKeyboardMarkup(row_width=1)
    reply_markup.add(
        types.InlineKeyboardButton("Advent Calеndar IT MY HUB", web_app=WebAppInfo(url))
    )
    bot.send_message(m.chat.id, message, reply_markup=reply_markup, parse_mode='HTML')
    bot.set_chat_menu_button(chat_id=m.chat.id, menu_button=MenuButtonWebApp(text='Calendar', web_app=WebAppInfo(url), type='web_app'))
