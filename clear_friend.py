import vk_api
"""
(Очистка Друзей)
Получение токена: https://vkhost.github.io/
pip install vk_api
"""
vk=vk_api.VkApi(token="ТОКЕН")

fg = vk.method("friends.get")# получаем список друзей
spisok_id = fg['items']# берём их айди

print("[START]")
for list_id in spisok_id:# каждый айди проверяем из списка
    check_users = vk.method("users.get",{"user_ids":list_id})# получаем инфу о пользователе

    if 'deactivated' in check_users[0]:# если он заморожен/удалён/заблокирован то
        # Этот метод БАНИТ его (в ЧС)
        #ban = vk.method("account.ban",{"owner_id":check_users[0]['id']})
        #print("+ Baned user: {} {}".format(check_users[0]['first_name'],check_users[0]['last_name']))

        # Этот метод УДАЛЯЕТ его
        delete = vk.method("friends.delete",{"user_id":check_users[0]['id']})
        print("+ Delete user: {} {}".format(check_users[0]['first_name'],check_users[0]['last_name']))

print("[DONE]")