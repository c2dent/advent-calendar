import html

from django.utils import timezone
from telebot import TeleBot
from telebot.types import InputMediaPhoto

from .models import PlannedMessage, TgUser
from .models.message_image import MessageImage


def send_planned_messages(bot: TeleBot):
    messages = PlannedMessage.objects.filter(send_time__lte=timezone.now(), is_sent=False)
    for message in messages:
        message_text = message.text.replace('<p>', '').replace('</p>', '').replace('<br />', '')
        message_text = html.unescape(message_text)

        additional_text = None
        if message.additional_info is not None and message.additional_info != "":
            additional_text = message.additional_info.replace('<p>', '').replace('</p>', '').replace('<br />', '')
            additional_text = html.unescape(additional_text)

        photos = []
        for image in MessageImage.objects.filter(message=message):
            photos.append(open(image.image.path, 'rb'))

        if len(photos) == 0:
            return

        for user in TgUser.objects.all():
            medias = []

            for photo_data in photos:
                if len(medias) == 0:
                    medias.append(InputMediaPhoto(photo_data, caption=message_text, parse_mode='HTML'))
                else:
                    medias.append(InputMediaPhoto(photo_data))

            bot.send_media_group(user.user_id, medias)

            for photo_data in photos:
                photo_data.seek(0)

            if additional_text is not None:
                bot.send_message(user.user_id, additional_text, parse_mode='HTML')

        message.is_sent = True
        message.save()
