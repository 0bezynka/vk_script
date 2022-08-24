import vk_api
import time
"""
(Вечный Онлайн)
"""
vk=vk_api.VkApi(token="ТОКЕН")

while True:
    vk.method("account.setOnline")# Онлайн
    print("Онлайн обновлён!")
    time.sleep(240)# Время
