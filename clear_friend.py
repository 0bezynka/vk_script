import vk_api
"""
(Очистка Друзей)
"""
vk=vk_api.VkApi(token="TOKEN")

fg = vk.method("friends.get")# получаем список друзей
spisok_id = fg['items']# берём их айди

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
        #print("+ Baned user: {} {}".format(check_users[0]['first_name'],check_users[0]['last_name']))

        # Этот метод УДАЛЯЕТ его
        delete = vk.method("friends.delete",{"user_id":check_users[0]['id']})
        d_chet += 1 # счётчик удалённых пользователей
        print("+ Delete user: {} {}".format(check_users[0]['first_name'],check_users[0]['last_name']))

print(f"[DONE] Удалено {d_chet} пользователей!")
