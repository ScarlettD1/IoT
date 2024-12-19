Запустить контейнер под mosquitto
python manage.py migrate - создать таблицы
py manage.py createsuperuser  - создать админскую учетную запись
python manage.py runserver  - запустить сервер

перейти на http://127.0.0.1:8000/admin
зайти в учетную запись админа
Заполнить таблицы:
  HoodActuatorConfig             = minval - 40; fan speed - 10
  LampActuatorConfig             = val - 6000
  TemperatureNotificationConfig  = threshhold - 24,0; isExcess - true; text - Temp is too hot (Можно создать несколько)
  WateringActuatorConfig         = min - 10; max - 20

Есть страницы с графиками:
  humidity-chart/
  illuminance-chart/
  moisture-chart/
  temperature-chart/
Для демонстрации работы сенсоров необходимо запусить интересующий скрипт в папке sensor, внутри есть http папка, где реализовано все посредством http запросов
