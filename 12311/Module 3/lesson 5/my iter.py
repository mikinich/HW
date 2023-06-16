import random


class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit
        return self
    def __next__(self):
        if self.limit == 0 :
            raise StopIteration
        self.limit -=1
        return random.randint(0, 100)
for i in RandomIter(10):
    print(i)