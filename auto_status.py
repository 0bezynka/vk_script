from random import choice
import vk_api, time

vk=vk_api.VkApi(token="TOKEN") # VK token

text = ['text1','text2','text3'] # СПИСОК

while True:
    r_text = (choice(text)) # СЛУЧАЙНЫЕ ТЕКСТ ИЗ СПИСКА
    SS = vk.method("status.set",{"text":r_text}) # УСТАНОВКА СТАТУСА

    time.sleep(270) # СОН 5 МИНУТ