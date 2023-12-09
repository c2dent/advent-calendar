## Команды

1. `run_bot`: Запускает телеграм бот.
2. `run_task`: Каждую минуту проверяет "Планированное сообщение". Если найдет, будет отправлять сообщение пользователям.

## Команда Django

Запустите следующую команду для языка на Django admin:

```bash
python manage.py makemessages -a; python manage.py compilemessages


В файле `config.yaml`, который находится в корневой директории проекта, 
укажите токен телеграм бота и хост, который будет работать миниапп.