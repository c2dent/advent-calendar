from django.db import models
from djrichtextfield.models import RichTextField


class PlannedMessage(models.Model):
    message_image = models.ImageField(upload_to='upload/', verbose_name='Баннер сообщении')
    text = RichTextField(max_length=4000)
    is_sent = models.BooleanField(default=False)
    send_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщении'
