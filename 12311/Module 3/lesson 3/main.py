token = 'vk1.a.lR7RXmTGfDoqO4j6vLs6-PniFoUSW4EiOya83KnDERpsH60ivuKugaRKGNQlE82ZrawS-JKkE8sxlxXJwCXKBbRvT7-8o7kKG4B5bOIEQt7C6hoMH0ak8E4X4l2Vz5_785HFQOe0ChhSVIUJjobd-ps6eo2yPjeHxxl-aVYZMJ7nW3d6DbiHsUbe2z7qzNoLuoKGjawu52wjnBXBmVtQ2g'


import vk_api
from wiki import get_article
from course2 import get_course
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint as rn
from SWAPI import get_fastest_ship
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        print(event.text)
        user_message = event.text.lower()
        user_id = event.user_id
        if user_message[:2] =='-к':
            value_name = user_message[3:].upper()
            response = get_course(value_name)
        elif user_message[:2] == '-в':
            article = user_message[2:]
            response = get_article(article)
        elif user_message[:8] == 'корабли':
            response =  get_fastest_ship()

        else: response = 'Я не знаю такую команду'
        vk.messages.send(
            user_id =user_id,
            message = response,
            random_id = rn(-10**7, 10**7)
        )
