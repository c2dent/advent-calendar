import html

from django.utils import timezone
from telebot import TeleBot
from telebot.types import InputMediaPhoto

from .models import PlannedMessage, TgUser
from .models.message_image import MessageImage
from .models.tg_message import TgMessage


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

            try:

                for photo_data in photos:
                    photo_data.seek(0)

                for photo_data in photos:
                    if len(medias) == 0:
                        medias.append(InputMediaPhoto(photo_data, caption=message_text, parse_mode='HTML'))
                    else:
                        medias.append(InputMediaPhoto(photo_data))

                tg_message = bot.send_media_group(user.user_id, medias)
                msg = TgMessage(message_id=tg_message[0].message_id, planned_message=message, tg_user=user, created_at=timezone.now())
                msg.save()

                if additional_text is not None:
                    tg_message = bot.send_message(user.user_id, additional_text, parse_mode='HTML')
                    msg = TgMessage(message_id=tg_message.message_id, planned_message=message, tg_user=user, created_at=timezone.now())
                    msg.save()

            except Exception as e:
                print(f"{user.user_id}")
                print(e)

        message.is_sent = True
        message.save()
