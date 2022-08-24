import vk_api
"""
ДОБАВЛЕНИЕ НОВЫХ ДРУЗЕЙ
"""

vk=vk_api.VkApi(token="TOKEN") # VK token

def friend_added():
	Chet_FGR = 0 # счётчик №1
	print("[ START ]")
	
	# Проверка входящих заявок 
	FGR = vk.method("friends.getRequests")
	
	if FGR['count'] > 0: # Если заявки есть то ...
		for items in FGR['items']:
			FA = vk.method("friends.add",{"user_id":items}) # Одобрение заявки
			Chet_FGR += 1 # счётчик №1
		print(f"[{Chet_FGR}] Заявок одобрено!")
	
	# Отправка заявок
	FGS = vk.method("friends.getSuggestions",{"filter":"mutual","count":50}) # Возможные друзья
	spisok_FGS = (FGS['items'])
	box1 = []

	for i in spisok_FGS:
		box1.append(i['id'])# ПОПЛНЯЕТ СПИСОК

	chet = 0 # счётчик №2
	for add in box1:
		chet += 1 # счётчик №2
		FGS = vk.method("friends.add",{"user_id":add})# ДОБОВЛЕНИЕ ДР
		UG= vk.method("users.get",{"user_ids":add})# ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ
		
		print(f"[{chet}] Заявка отправлена - {UG[0]['first_name']} {UG[0]['last_name']}")
		time.sleep(5)
