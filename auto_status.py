from random import choice
import vk_api, time
"""
Авто-Статус 
"""

vk=vk_api.VkApi(token="TOKEN")
# Список
text = ['text1','text2','text3']

while True:
    # Случайный текст из списка
    r_text = (choice(text))
    # Установка статуса
    vk.method("status.set",{"text":r_text})
    print("Статус обновлён!")

    time.sleep(300) # Сон 5 минут
