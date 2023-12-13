from django.core.exceptions import ValidationError
from django.db import models
from djrichtextfield.models import RichTextField


class PlannedMessage(models.Model):
    text = RichTextField(max_length=1010, verbose_name="Текст под баннер")
    additional_info = RichTextField(max_length=4000, verbose_name="дополнительный текст", null=True, blank=True)
    is_sent = models.BooleanField(default=False, verbose_name="Отправлено")
    send_time = models.DateTimeField(verbose_name="Время отправки")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщении'
