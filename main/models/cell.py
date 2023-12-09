from django.db import models
from djrichtextfield.models import RichTextField


class Cell(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер ячейки')
    description = models.CharField(verbose_name='Содержимое', max_length=250)
    message_image = models.ImageField(upload_to='upload/', verbose_name='Баннер сообщении')
    webapp_image = models.ImageField(upload_to='upload/', verbose_name='Фото миниапп')
    content = RichTextField(max_length=4000)
    open_date = models.DateField(verbose_name="Когда будет доступен")

    class Meta:
        verbose_name = 'Ячейка'
        verbose_name_plural = 'Ячейки'

    def __str__(self):
        return f"номер: {self.number} дата: {self.open_date.day}.{self.open_date.month}"
