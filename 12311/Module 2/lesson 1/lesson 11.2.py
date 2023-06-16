class Singleton:
    __instance =None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)


        return cls.__instance

    def __init__(self, a,b):
        self.a = a
        self.b = b
a = Singleton(10,20)
b = Singleton(30, 40)

def timer(funk):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funk(*args, **kwargs)
        print('Прошло времени:', time.time() - start)
        return result
    return wrapper()

import time
@timer
def get_list_by_default_way(val):
    my_list = []
    for i in range(val):
        my_list.append(i)
    return my_list
@timer
def get_list_by_list_comp(val):
    my_list = [i for i in range(val)]
    return my_list

get_list_by_list_comp(10 ** 16 *5)
get_list_by_default_way(10 ** 16 *5)