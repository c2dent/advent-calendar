import html

from django.utils import timezone
from telebot import TeleBot

from .models import PlannedMessage, TgUser


def send_planned_messages(bot: TeleBot):
    messages = PlannedMessage.objects.filter(send_time__lte=timezone.now(), is_sent=False)
    for message in messages:
        message_text = message.text.replace('<p>', '').replace('</p>', '').replace('<br />', '')
        message_text = html.unescape(message_text)

        additional_text = None
        if message.additional_info is not None and message.additional_info != "":
            additional_text = message.additional_info.replace('<p>', '').replace('</p>', '').replace('<br />', '')
            additional_text = html.unescape(additional_text)

        photo = open(message.message_image.path, 'rb')
        for user in TgUser.objects.all():
            bot.send_photo(user.user_id, photo, caption=message_text, parse_mode='HTML')
            photo.close()

            if additional_text is not None:
                bot.send_message(user.user_id, additional_text, parse_mode='HTML')

        message.is_sent = True
        message.save()
