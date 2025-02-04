import vk_api
from config import *
"""
Очистка  стены
"""

vk=vk_api.VkApi(token=TOKEN)

def clear_wall():
    # Получем все записи
    get_wall_posts = vk.method("wall.get",{'filter':'all'})['items']
    
    for info  in get_wall_posts:
        # Берем айди записи
        post_id = info['id']
        vk.method("wall.delete", {'post_id':post_id})
        print("Запись удалена:", post_id)