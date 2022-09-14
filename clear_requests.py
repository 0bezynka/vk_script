import vk_api, time

vk=vk_api.VkApi(token="TOKEN") # VK

def banneduser():
	chet = 0
	FGR = vk.method("friends.getRequests",{"out":1}) # Исходящие заявки
	for i in FGR['items']:
		vk.method("friends.delete",{"user_id":i}) # Добавление в ЧС
		chet += 1
		print(f"[{chet}] Banned user")
		time.sleep(2)

banneduser()
