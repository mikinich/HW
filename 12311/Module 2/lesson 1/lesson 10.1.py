# class A:
#     def info(self):
#         print('это класс А')
#
#
#
# class B(A):
#     pass
#
#
#
#
# a = A()
# a.info()
#
# b = B()
# b.info()






class Pet:
    has_tail = True
    legs = 4
    name = None
    animal = None

    def __str__(self):
        result = f'Питомец {self.name} это {self.animal}. ' \
            f"у него {'есть хвост' if self.has_tail else 'хвоста нет' }. У него {self.legs} ног(и)"
        return result

    def sound(self):
        pass


class Dog(Pet):
    name = 'Чарли'
    animal = 'Собака'

    def sound(self):
        return 'ГАФ!'










class Frog(Pet):
    has_tail = False
    name = 'пепе'
    animal = 'лягушка'

    def sound(self):
        return 'КВА!'
print(Dog(), Dog().sound())
print(Frog(), Frog().sound())
a=19
b=5
