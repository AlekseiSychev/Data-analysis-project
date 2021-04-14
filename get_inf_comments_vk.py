'''
Написать скрипт, который выводит в консоль комментарии к указанному посту.

'''

import requests
from vk_config import VK_CONFIG

def comments_vk():
    # Пример запроса к API: https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V

    domain = VK_CONFIG['domain']
    access_token = VK_CONFIG['access_token']
    method_name = 'wall.getComments'
    V = VK_CONFIG['V']
    owner_id = -1 # id Сообщества тестовое значение
    post_id = 394899 # id Поста тестовое значение

    query = f"{domain}/{method_name}?owner_id={owner_id}&post_id={post_id}&access_token={access_token}&v={V}"
    response = requests.get(query)
    r = response.json()
    
    if 'response' in r:
        if 'items' in r['response']:
            try:
                for com in r['response']['items']:
                    print(com['text'])
            except(KeyError):
                return False

    return comments_vk

if __name__ == "__main__":
    comments_vk()