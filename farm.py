from pprint import pprint

class Animals:
    name = 'Name'
    weight = 0
    appetite = 'hungry'

    def food(self):
        """Кормим животное"""
        self.appetite = 'fed'


class Goose(Animals):
    laying_hen = 'no_egged'

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'


class Cow(Animals):
    condition = 'full'

    def milk(self):
        """Доим"""
        self.condition = 'empty'

class Sheep(Animals):
    hair_style = 'shaggy'

    def cut(self):
        """Стрижем"""
        self.hair_style = 'bald'

class Chicken(Animals):
    laying_hen = 'no_egged'

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'

class Goat(Animals):
    condition = 'full'

    def milk(self):
        """Доим"""
        self.condition = 'empty'

class Duck(Animals):
    laying_hen = 'no_egged'

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'

pprint(Animals.__dict__)
print(Cow.__dict__)
print(Goose.__dict__)




