import vk_api, time
"""
(Вечный Онлайн)
"""
vk=vk_api.VkApi(token="ТОКЕН")

while True:
    vk.method("account.setOnline")# Онлайн
    print("Онлайн обновлён!\nСон 5 минут")
    time.sleep(240)# Время
