from django.db import models

from main.models.common import CellStatus


class UserCell(models.Model):
    tg_user = models.ForeignKey('main.TgUser', verbose_name='Пользователь', on_delete=models.CASCADE)
    cell = models.ForeignKey('main.Cell', verbose_name='Ячейке', on_delete=models.CASCADE)
    is_opened = models.BooleanField(default=False)

