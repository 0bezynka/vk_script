import vk_api
import time
"""
(Вечный онлайн)
Получение токена: https://vkhost.github.io/
pip install vk_api
"""
vk=vk_api.VkApi(token="ТОКЕН")

while True:
    vk.method("account.setOnline")# Онлайн
    time.sleep(240)# Время