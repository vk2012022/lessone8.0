from abc import ABC, abstractmethod

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def changeWeapon(self):
        self.weapon.attack(self)

class Monster():
    def __init__(self, name):
        self.name = name

class Weapon(ABC):
    @abstractmethod
    def attack(self, weapon):
        pass


class Sword(Weapon):
    def attack(self, weapon):
        print(f"Богатырь {fighter.name} выбирает меч.\n{fighter.name} наносит удар мечом.")
        print(f"{monster.name} побежден!")

class Bow(Weapon):
    def attack(self, weapon):
        print(f"Богатырь {fighter.name} выбирает лук.\n{fighter.name} наносит удар из лука.")
        print(f"{monster.name} побежден!")

fighter = Fighter("Илья Муромец", Sword())
monster = Monster("Соловей Разбойник")
fighter.changeWeapon()

fighter = Fighter("Алеша Попович", Bow())
monster = Monster("Дракон")
fighter.changeWeapon()
