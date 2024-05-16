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
    def attack(self, fighter):
        pass

class Sword(Weapon):
    def attack(self, fighter):
        print(f"Богатырь {fighter.name} выбирает меч.\n{fighter.name} наносит удар мечом.")
        print(f"{monster.name} побежден!")

class Bow(Weapon):
    def attack(self, fighter):
        print(f"Богатырь {fighter.name} выбирает лук.\n{fighter.name} наносит удар из лука.")
        print(f"{monster.name} побежден!")

# Пример использования
monster = Monster("Соловей Разбойник")
fighter = Fighter("Илья Муромец", Sword())
fighter.changeWeapon()

monster = Monster("Дракон")
fighter = Fighter("Алеша Попович", Bow())
fighter.changeWeapon()

