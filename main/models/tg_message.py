from django.db import models


class TgMessage(models.Model):
    message_id = models.BigIntegerField()
    planned_message = models.ForeignKey('main.PlannedMessage', on_delete=models.CASCADE, verbose_name="Сообщение")
    tg_user = models.ForeignKey('main.TgUser', on_delete=models.CASCADE, verbose_name="Тг пользователь")
    created_at = models.DateTimeField(editable=False, null=True, default=None, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Отпр сообщения"
        verbose_name_plural = "Отпр сообщении"

    def __str__(self):
        return self.tg_user.first_name
