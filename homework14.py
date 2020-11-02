class Units:
    def __init__(self, name, clan, health, power, dext, intell):
        self.name = name
        self.clan = clan
        self.health = health
        self.power = power
        self.dext = dext
        self.intell = intell

    def health_increase(self):
        if self.health <= 90:
            self.health += 10


class Mage(Units):
    def __init__(self, name, clan, health, power, dext, intell, features):
        super().__init__(name, clan, health, power, dext, intell)
        self.features = 'air', 'fire', 'water'

    def increase_intell(self):
        if self.intell < 10:
            self.intell += 1

    def __repr__(self):
        return f"Name:{self.name},Clan:{self.clan}, Health:{self.health}, Power:{self.power}, Dexterity:{self.dext}, Intelligence:{self.intell}, Features:{self.features}"
result = Mage('john', 'mage', health=55, power=10, dext=10, intell=7, features= ('air', 'fire', 'water'))
result.health_increase()
result.increase_intell()
print(result)
class Archer(Units):
    def __init__(self, name, clan, health, power, dext, intell, feature):
        super().__init__(name, clan, health, power, dext, intell)
        self.feature = 'bow', 'crossbow'

    def increase_dext(self):
        if self.dext < 10:
            self.dext += 1

    def __repr__(self):
        return f"Name:{self.name},Clan:{self.clan}, Health:{self.health}, Power:{self.power}, Dexterity:{self.dext}, Intelligence:{self.intell}, Features:{self.feature}"

result = Archer('Valter', 'archer', health=67, power=6, dext=3, intell=1, feature= ('bow', 'crossbow'))
result.increase_dext()
result.health_increase()
print(result)


class Knight(Units):
    def __init__(self, name, clan, health, power, dext, intell, feature):
        super().__init__(name, clan, health, power, dext, intell)
        self.feature = 'sword', 'axe', 'lance'

    def increase_power(self):
        if self.power < 10:
            self.power += 1

    def __repr__(self):
        return f"Name:{self.name},Clan:{self.clan}, Health:{self.health}, Power:{self.power}, Dexterity:{self.dext}, Intelligence:{self.intell}, Features:{self.feature}"
result = Knight(name='Lancelot', clan='knight', health=3, power=4, dext=1, intell=1, feature=('sword', 'axe', 'lance'))

result.health_increase()
result.increase_power()
print(result)







