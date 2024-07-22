import vk_api, config
from datetime import datetime
import random, time

vk=vk_api.VkApi(token=config.TOKEN)

# Сборник методов + твоя креативность = тот самый результат
def box():
    text_for_status = ""

    if config.TIME:
        now = datetime.now()
        text_for_status += f"На часах: {now.strftime('%H:%M')} А сегодня: {now.strftime('%d.%m.%Y')} | "
    
    if config.LIKE_AVA:
        get_count_like = vk.method('photos.get', {'album_id': 'profile', 'rev': 1, 'extended': 1, 'count': 1})
        text_for_status += f"На аве: {get_count_like['items'][0]['likes']['count']} 🖤 | "
    
    if config.FOLLOWERS:
        get_count_followers = vk.method('users.getFollowers')
        text_for_status += f"Подписчиков: {get_count_followers['count']} | "
    
    if config.NEW_MESSAGE:
        get_new_message = vk.method('account.getCounters', {"filter":"messages"})
        text_for_status += f"Новых сообщений: {get_new_message['messages']} | "
    
    if config.NEW_FRIENDS:
        get_new_friends = vk.method('account.getCounters', {"filter":"friends"})
        text_for_status += f"Заявок в др: {get_new_friends['friends']} | "
    
    if config.BANNED:
        get_banned = vk.method('account.getBanned',{'count':0})
        text_for_status += f"В ЧС: {get_banned['count']} | "
    
    if config.FRIENDS_ONLINE:
        get_friends_online = vk.method('friends.getOnline')
        text_for_status += f"Друзей онлайн: {len(get_friends_online)} | "
    
    
    # Ставим статус
    vk.method("status.set",{"text":text_for_status})

# Словарь для замены цифр
numbers = {'0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣', '4': '4⃣',
           '5': '5⃣', '6': '6⃣', '7': '7⃣','8': '8⃣', '9': '9⃣'}

# Ниже пару примеров
def primer_1():
    heart_smile = ["❤","💙","🖤","💚","💜","🧡","💛"]
    
    text_for_status = ""

    if config.TIME:
        now = datetime.now()
        text_for_status += f"Сейчас 🕰: {now.strftime('%H:%M')} | "
        # Вот здесь преобразование цифр происходит
        if config.RECONSTRUCT:
            for number in numbers:
                text_for_status = text_for_status.replace(number, numbers[number])
    
    if config.LIKE_AVA:
        get_count_like = vk.method('photos.get', {'album_id': 'profile', 'rev': 1, 'extended': 1, 'count': 1})
        text_for_status += f"На аве {get_count_like['items'][0]['likes']['count']} {random.choice(heart_smile)} | "
    
    if config.FRIENDS_ONLINE:
        get_friends_online = vk.method('friends.getOnline')
        text_for_status += f"👥 онлайн {len(get_friends_online)} | "
    
    if config.NEW_MESSAGE:
        get_new_message = vk.method('account.getCounters', {"filter":"messages"})
        text_for_status += f"Новых 📩 {get_new_message['messages']} | "
    
    vk.method("status.set",{"text":text_for_status})

def primer_2():
    text_for_status = ""

    if config.TIME:
        now = datetime.now()
        text_for_status += f"Сейчас ⏳ {now.strftime('%H:%M')} | 📅 {now.strftime('%d.%m.%Y')} "
        # Вот здесь преобразование цифр происходит
        if config.RECONSTRUCT:
            for number in numbers:
                text_for_status = text_for_status.replace(number, numbers[number])
    
    vk.method("status.set",{"text":text_for_status})

def primer_3():
    loading = 1
    
    while True:
        if loading > 100:
            loading = 1
        else:
            vk.method("status.set",{"text":f"Загрузка... ████████████] {loading}%"})
            loading += 1
        
        time.sleep(300)