<h1 align="center">Об скриптах</h1>

### Вечный Онлайн
Метод помечает пользователя "Онлайн" на 5 минут. Скрипт срабатывает каждые 5 минут. Тем самым пользователь "вечно онлайн".
```bash
python online.py
```
### Очистка Друзей
Находит забаненых/удалённых пользователей в друзьях. На выбор удаляет или банит (в ЧС) пользователя. Оба метода в скрипте, нужно лишь убрать "#" комментарий нужного метода. Должен работать один из них!
```bash
python clear_friend.py
```
### Авто-статус
Самый простой скрипт Авто-статуса, из всего списка выбирает случайные текст, который в дальнейшем устанвливается "статусом" страницы вк.
Отталкиваясь от этого исходника, можно сделать множество вариаций "статуса", все ограничивается фантазией.
```bash
python auto_status.py
```
### Добавление друзей
Сначала одобряет входящие заявки  (при их наличии). Затем получает список "возможных" друзей в кол-во 50-и пользователей (больше нету смысла, т.к. более 50 заявок в сутки отправить ВК не позволит), отправляет заявки предложенным пользователям.
```bash
python add_friend.py
```
### Сохранение диалогов
В файл (.txt) сохраняет все диалоги которые есть на данный момент. Лично мне надо был скрипт для обучения чат-бота. Это голый скрипт, под свои нужды его необходимо дорабатывать.
```bash
python get_history_chat.py
```
### Очитска стены
После запуска скрипта все записи на стене будут удалены.
```bash
python clear_wall.py
```

![language](https://img.shields.io/badge/python-3.10-purple) ![library](https://img.shields.io/badge/library-vk_api-blue)
---

> Надеюсь тебе пригодится. Все скрипты здесь для тех кто знает что с ними делать и как применять.
> 
> Связь со мной [VK](https://vk.com/id755728119)
