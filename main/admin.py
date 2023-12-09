from django.contrib import admin

from main.models import TgUser, UserCell, PlannedMessage
from main.models.cell import Cell


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ['number', 'open_date']


@admin.register(TgUser)
class Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_id']


@admin.register(PlannedMessage)
class PlannedMessageAdmin(admin.ModelAdmin):
    list_display = ['is_sent', 'send_time']
#
#
# @admin.register(UserCell)
# class Admin(admin.ModelAdmin):
#     list_display = ['is_opened']
