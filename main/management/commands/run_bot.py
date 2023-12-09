import signal
import sys

import telebot
from django.conf import settings
from django.core.management import BaseCommand

from main.services.telegram.commands.start import start


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
        bot.register_message_handler(start, commands=['start'], func=lambda m: m.chat.type == 'private', pass_bot=True)

        def exit_gracefully(*args):
            print('Завершение по kill!', args)
            bot.stop_polling()
            print('Завершено 1')
            sys.exit(0)

        signal.signal(signal.SIGINT, exit_gracefully)
        signal.signal(signal.SIGTERM, exit_gracefully)

        print('Запуск бота')
        bot.infinity_polling()
