import vk_api, time
"""
Отменяет все исходящие заявки
"""
vk=vk_api.VkApi(token="TOKEN") # VK

def clear_requests():
	chet = 0
	FGR = vk.method("friends.getRequests",{"out":1}) # Исходящие заявки
	for i in FGR['items']:
		vk.method("friends.delete",{"user_id":i}) # Удаляет пользователя
		chet += 1
		print(f"[{chet}] Отменил заявку")
		time.sleep(1)

clear_requests()
