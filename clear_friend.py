import vk_api
from config import *
"""
Очистка друзей
"""
vk=vk_api.VkApi(token=TOKEN)

# Получаем список друзей
fg = vk.method("friends.get")
# Берём их айди
spisok_id = fg['items']

chet = 0 # счётчик
d_chet = 0 # счётчик удалённых пользователей

print("[START]")
for list_id in spisok_id:# каждый айди проверяем из списка
    check_users = vk.method("users.get",{"user_ids":list_id})# получаем инфу о пользователе
    chet += 1
    print(f"{chet} - Проверяю пользователя")

    if 'deactivated' in check_users[0]:# если он заморожен/удалён/заблокирован то
        # Этот метод БАНИТ его (в ЧС) 
        #ban = vk.method("account.ban",{"owner_id":check_users[0]['id']})
        #d_chet += 1 # счётчик удалённых пользователей
        #print("+ Заблокировал: {} {}".format(check_users[0]['first_name'],check_users[0]['last_name']))

        # Этот метод УДАЛЯЕТ его
        delete = vk.method("friends.delete",{"user_id":check_users[0]['id']})
        d_chet += 1 # счётчик удалённых пользователей
        print("+ Удалил: {} {}".format(check_users[0]['first_name'],check_users[0]['last_name']))

print(f"[FINISH] Удалено {d_chet} пользователей!")
