token = 'vk1.a.lR7RXmTGfDoqO4j6vLs6-PniFoUSW4EiOya83KnDERpsH60ivuKugaRKGNQlE82ZrawS-JKkE8sxlxXJwCXKBbRvT7-8o7kKG4B5bOIEQt7C6hoMH0ak8E4X4l2Vz5_785HFQOe0ChhSVIUJjobd-ps6eo2yPjeHxxl-aVYZMJ7nW3d6DbiHsUbe2z7qzNoLuoKGjawu52wjnBXBmVtQ2g'


import vk_api
import random as rn
from CB_RF import Dollar_course
from SWAPI import MAX_D
vk = vk_api.VkApi(token=token)
while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter' : 'unanswered' })
    if messages['count'] >0:
        message_text = messages['items'][0]['last_message']['text']
        if message_text =="планета":
           ans = f'самый большой диаметр у планеты это {MAX_D()}'
        elif message_text == 'курс':
            ans = f'курс доллара на сегодня составляет {Dollar_course()} руб.'
        else:
            ans = 'неизвестная команда'

        user_id = messages['items'][0]['last_message']['from_id']
        random_id = rn.randint(-10 **7, 10 **7)
        vk.method('messages.send', {
            'user_id' : user_id,
            'random_id' : random_id,
            'message' : ans
        })
