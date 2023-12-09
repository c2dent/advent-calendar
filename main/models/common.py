from django.db import models


class CellStatus(models.TextChoices):
    OPENED = 'OPENED', 'Открыто'
    READY_TO_OPEN = 'READY_TO_OPEN', 'Готов к открытыю'
    CLOSED = 'CLOSED', 'Закрытий'
