import vk_api, time
from config import *
"""
Добавление новых друзей 
"""

vk=vk_api.VkApi(token=TOKEN)

def adding_friends():
	chet = 1
	# Возможные друзья - 50 чел
	get_info = vk.method('friends.getSuggestions',{'count':50})
	# Список айди
	id_user = get_info['items']
	for user in id_user:
		# Отправка заявки
		vk.method("friends.add",{"user_id":user['id']})
		print(f"[ #{chet} ] Отправил заявку: {user['first_name']} {user['last_name']}")
		chet += 1

		time.sleep(2)
