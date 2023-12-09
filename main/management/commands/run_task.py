import time

import telebot
from django.conf import settings
from django.core.management import BaseCommand

from main.tasks import send_planned_messages


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
        try:
            while True:
                send_planned_messages(bot)
                time.sleep(60)
        except KeyboardInterrupt:
            print("Остановка задачи...")
