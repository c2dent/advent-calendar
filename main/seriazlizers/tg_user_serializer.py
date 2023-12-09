from rest_framework import serializers

from main.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ['id', 'user_id', 'first_name']
