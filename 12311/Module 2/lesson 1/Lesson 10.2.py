class tank:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def shoot(self, enemy):
        enemy.health_down(enemy.damage)
        print(f"Мы выстрелили по {enemy}")
    def health_down(self, damage):
        total_damage = damage /self.armor
        self.hp -= total_damage
        print(f"По нам попали на {damage}")







class T34(tank):
    def __str__(self):
        return 'Т34'


class KV44(tank):
    def __init__(self, hp, damage, armor):
        super().__init__(hp, armor * 10, damage * 100 )
    def __str__(self):
        return 'КВ 44'






t34 =T34(1000, 1500,200)
kv44 = KV44(1000, 500, 100)

t34.shoot(kv44)
kv44.shoot(t34)