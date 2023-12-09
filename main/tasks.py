from django.utils import timezone
from telebot import TeleBot

from .models import PlannedMessage, TgUser


def send_planned_messages(bot: TeleBot):
    messages = PlannedMessage.objects.filter(send_time__lte=timezone.now(), is_sent=False)
    for message in messages:
        photo = open(message.message_image.path, 'rb')
        for user in TgUser.objects.all():
            bot.send_photo(user.user_id, photo)
            bot.send_message(user.user_id, message.text)
        message.is_sent = True
        message.save()
