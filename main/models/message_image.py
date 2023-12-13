from django.db import models


class MessageImage(models.Model):
    message = models.ForeignKey('main.PlannedMessage', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/')

    class Meta:
        verbose_name = "карточка сообщении"
        verbose_name_plural = "карточки сообщении"
