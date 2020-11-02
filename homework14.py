class Units:
    def __init__(self, name, clan, health, power, dext, intell):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 10
        self.dext = 10
        self.intell = 10

    def health_increase(self):
        if self.health <= 90:
            self.health += 10

    def __repr__(self):
        return f" {self.name}{self.clan}{self.health}{self.power}{self.dext}{self.intell}"


class Mage(Units):
    def __init__(self, name, clan, health, power, dext, intell, feature):
        super().__init__(self, name, clan, health, power, dext, intell)
        self.feature = 'air', 'fire', 'water'

    def __repr__(self):
        return f" {self.name}{self.clan}{self.health}{self.power}{self.dext}{self.intell}"




class Archer(Units):
    def __init__(self, name, clan, health, power, dext, intell, feature):
        super().__init__(self, name, clan, health, power, dext, intell)
        self.feature = 'bow', 'crossbow'

class Knight:
    def __init__(self, name, clan, health, power, dext, intell, feature):
        super().__init__(self, name, clan, health, power, dext, intell)
        self.type = 'sword', 'axe', 'lance'








