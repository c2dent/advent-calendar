from telebot import types

from main.models import TgUser, Cell, UserCell


class TgUserService:

    @classmethod
    def get_or_create(cls, m: types.Message):
        exists = TgUser.objects.filter(user_id=m.chat.id).exists()

        user = None
        if exists is False:
            user = TgUser(user_id=m.chat.id, first_name=m.chat.first_name, last_name=m.chat.last_name, username=m.chat.username)
            user.save()
        else:
            user = TgUser.objects.filter(user_id=m.chat.id).first()
        return user

    @classmethod
    def create_if_not_user_cell(cls, cell: Cell, user: TgUser):
        exists = UserCell.objects.filter(cell_id=cell.id, tg_user_id=user.id).exists()
        if exists is True:
            return

        user_cell = UserCell(cell=cell, tg_user=user)
        user_cell.save()
