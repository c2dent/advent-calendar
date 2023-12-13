from django.db import models


class TgUser(models.Model):
    user_id = models.BigIntegerField(verbose_name='Ид в телеграмм', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', null=True, blank=True, max_length=60)
    username = models.CharField(verbose_name="tg username", null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = 'Телеграм пользователь'
        verbose_name_plural = 'Телеграм пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
