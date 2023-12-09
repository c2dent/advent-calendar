from rest_framework import serializers

from main.models import UserCell
from main.seriazlizers.cell_serializer import CellSerializer
from main.seriazlizers.tg_user_serializer import TgUserSerializer


class UserCellSerializer(serializers.ModelSerializer):
    tg_user = TgUserSerializer()
    cell = CellSerializer()

    class Meta:
        model = UserCell
        fields = ['id', 'tg_user', 'cell', 'is_opened']
