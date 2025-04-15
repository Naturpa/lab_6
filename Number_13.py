class Weapon:
    def __init__(self, name, damage, range):
        self.name, self.damage, self.range = name, damage, range

    def hit(self, actor, target):
        if not target.is_alive():
            print('Враг уже повержен')
        else:
            x1, y1 = actor.get_coords()
            x2, y2 = target.get_coords()
            if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 > self.range:
                print(f'Враг слишком далеко для оружия {self.name}')
            else:
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y, self.hp = pos_x, pos_y, hp

    def move(self, delta_x, delta_y):
        pass

    def is_alive(self):
        if self.hp:
            return True
        else:
            return False

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = False
        return self.hp

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def move(self, pos_x, pos_y):
        self.x, self.y = pos_x, pos_y
        self.pos_x += self.x
        self.pos_y += self.y

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}'


class MainHero(BaseCharacter):
    weapon = 0

    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.weapon = None

    def hit(self, target):
        if not self.weapons:
            print('Я безоружен')
        elif isinstance(target, BaseEnemy):
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Врага')

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f'Подобрал {weapon}')
        if not self.weapon:
            self.weapon = weapon

    def next_weapon(self):
        if not self.weapons:
            print('Я безоружен')
        elif self.weapons[0] == self.weapons[-1]:
            print('У меня только одно оружие')
        else:
            self.weapon = self.weapons[-1]
            print(f'Сменил оружие на {self.weapons[-1]}')

    def heal(self, amount):
        if self.hp != 200:
            self.hp += amount
            print(f'Полечился, теперь здоровья {self.hp}')


# Примеры использования:
weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
