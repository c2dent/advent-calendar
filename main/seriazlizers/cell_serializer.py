from django.utils import timezone
from rest_framework import serializers

from main.models import Cell


class CellSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField()

    class Meta:
        model = Cell
        fields = ['id', 'number', 'available', 'description', 'open_date', 'available', 'webapp_image']

    def get_available(self, obj):
        return timezone.now().date() >= obj.open_date
