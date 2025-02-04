import vk_api
from config import *
import os

print("# Начинаю")
vk=vk_api.VkApi(token=TOKEN)


# Создание папки
if not os.path.isdir(NAME_DIRECTORY):
    os.mkdir(NAME_DIRECTORY)
    print("# Папку создал")


# Возвращает информацию о текущем профиле
info_profile = vk.method("account.getProfileInfo")
name_profile = f"{info_profile['first_name']} {info_profile['last_name']}"
print("Аккаунт:", name_profile)

# Счетчик
chet = 1

# Сохранение диалогов
def save_in_file(id_user):
    try:
        # Возвращает информацию о пользователе
        info_user = vk.method("users.get", {'user_ids':id_user})[0]
        name_user = f"{info_user['first_name']} {info_user['last_name']}"
        print(f"[{chet}] Диалог с ", name_user)

        # История диалога
        history = vk.method("messages.getHistory",{'count':200, 'peer_id':id_user, 'rev':1})['items']

        # Запись в файл
        with open(f'{NAME_DIRECTORY}/{name_user}.txt', 'a', encoding="UTF-8") as file:
            for dialog in history:
                if dialog['from_id'] == id_user:
                    file.write(f"{name_user}: {dialog['text']} \n")
                else:
                    file.write(f"{name_profile}: {dialog['text']} \n")
    except IndexError:
        print("# Пропускаем", id_user)

# Получение всех чатов
get_chat = vk.method("messages.getConversations",{'count':200, 'filter':'all'})
print(f"Диалогов:", get_chat['count'])

for id_user in get_chat['items']:
    save_in_file(int(id_user['conversation']['peer']['id']))
    chet += 1

print("# Закончил!")