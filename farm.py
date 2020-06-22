class Animal:
    appetite = 'hungry'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def food(self):
        """Кормим животное"""
        self.appetite = 'fed'

    def heavyweight(self):
        heavy_name = ''
        max_weight = 0
        farm_weight = 0

        for item in self.joe_farm:
            farm_weight += item.weight
            if item.weight > max_weight:
                max_weight = item.weight
                heavy_name = f'{item.name}'
        return f'Общий вес животных на ферме {farm_weight} кг. Самое тяжелое животное - {heavy_name} с весом {max_weight} кг'

class Egg(Animal):
    laying_hen = 'no_egged'

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'


class Milk(Animal):
    condition = 'full'

    def milked(self):
        """Доим"""
        self.condition = 'empty'


class Wool(Animal):
    hair_style = 'shaggy'

    def cut(self):
        """Стрижем"""
        self.hair_style = 'bald'


class Goose(Egg):
    voice = "gnaws"


class Cow(Milk):
    voice = "groans"


class Sheep(Wool):
    voice = "bleats"


class Chicken(Egg):
    voice = "cackle"


class Goat(Wool, Milk):
    voice = "yell"


class Duck(Egg):
    voice = "quack"


goose0 = Goose('Gray', 4)
goose1 = Goose('White', 3)
cow0 = Cow('Manka', 720)
sheep0 = Sheep('Lamb', 70)
sheep1 = Sheep('Curly', 80)
chicken0 = Chicken('Ko_ko', 2)
chicken1 = Chicken('Kukareku', 3)
goat0 = Goat('Hooves', 50)
goat1 = Goat('Horns', 70)
duck0 = Duck('Mallard', 1)

joe_farm = {goose0, goose1, cow0, sheep0, sheep1, chicken0, chicken1, goat0, goat1, duck0}

farm = Animal(joe_farm)

print(farm.heavyweight())
