import vk_api, time
"""
Вечный онлайн
"""
vk=vk_api.VkApi(token="ТОКЕН")

while True:
    vk.method("account.setOnline")# Онлайн
    print("Онлайн обновлён!\nСон 5 минут")
    time.sleep(300)# Время
