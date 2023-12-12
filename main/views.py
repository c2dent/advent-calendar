import html
import json
import textwrap

import telebot
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.html import format_html

from main.models import TgUser, UserCell, Cell
from main.seriazlizers.user_cell_serializer import UserCellSerializer
from main.services.tg_user_service import TgUserService


def advent(request, user_id):
    user_exists = TgUser.objects.filter(user_id=user_id).exists()
    if user_exists is False:
        return render(request, '404.html', {}, status=404)

    user = TgUser.objects.filter(user_id=user_id).first()

    cells = Cell.objects.all()
    for item in cells:
        TgUserService.create_if_not_user_cell(cell=item, user=user)

    user_cells = UserCell.objects.filter(tg_user=user)
    serializer_data = json.dumps(UserCellSerializer(user_cells, many=True).data)
    return render(request, 'advent.html', {'data': serializer_data, 'user': user, 'cells': user_cells})


def send_message(request):
    user_id = request.GET.get('user_id')
    cell_id = request.GET.get('cell_id')
    user_exists = TgUser.objects.filter(user_id=user_id).exists()
    cell_exists = Cell.objects.filter(id=cell_id).exists()
    if user_exists is False or cell_exists is False:
        return

    user_cell = UserCell.objects.filter(tg_user__user_id=user_id, cell_id=cell_id).first()
    bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
    photo = open(user_cell.cell.message_image.path, 'rb')
    message_text = user_cell.cell.content.replace('<p>', '').replace('</p>', '').replace('<br />', '')
    message_text = html.unescape(message_text)
    bot.send_photo(user_id, photo, caption=message_text, parse_mode='HTML')
    photo.close()

    if user_cell.cell.additional_info is not None and user_cell.cell.additional_info != "":
        message_text = user_cell.cell.additional_info.replace('<p>', '').replace('</p>', '').replace('<br />', '')
        message_text = html.unescape(message_text)
        bot.send_message(user_id, message_text, parse_mode='HTML')

    user_cell.is_opened = True
    user_cell.save()
    return JsonResponse(data={})


def split_text(text, max_length):
    return textwrap.wrap(text, max_length)
