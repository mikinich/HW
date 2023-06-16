# Чтобы закрепить понятия наследования, можно дома попробовать реализовать простенькую игру:

# 1) Создать класс user со свойством здоровье и методом атаки и урона.

# 2) Создать классы маг, воин и лучник, которые наследуются от класса user.




class User:
    HP = None
    Damage = None
    AM = None
    def __str__(self):
        result = f"Герой имеет {self.HP} здоровья и бьёт на {self.Damage} урона, используя {self.AM}"
        return result


class Magitian(User):
    HP = 80
    Damage = 35
    AM = 'Заклинание'


class Warrior(User):
    HP = 100
    Damage = 45
    AM = 'Меч'


class Archer(User):
    HP = 90
    Damage = 35
    AM = 'Стрелы'

print(Magitian())
print(Warrior())
print(Archer())