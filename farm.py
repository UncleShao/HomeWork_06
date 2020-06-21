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
    voice = "gnaws"

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'


class Cow(Animals):
    condition = 'full'
    voice = "groans"

    def milk(self):
        """Доим"""
        self.condition = 'empty'


class Sheep(Animals):
    hair_style = 'shaggy'
    voice = "bleats"

    def cut(self):
        """Стрижем"""
        self.hair_style = 'bald'


class Chicken(Animals):
    laying_hen = 'no_egged'
    voice = "cackle"

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'


class Goat(Animals):
    condition = 'full'
    voice = "yell"

    def milk(self):
        """Доим"""
        self.condition = 'empty'


class Duck(Animals):
    laying_hen = 'no_egged'
    voice = "quack"

    def eggs(self):
        """Собираем яйца"""
        self.laying_hen = 'egged'


goose0 = Goose()
goose0.name = 'Gray'
goose0.weight = 4  # kg

goose1 = Goose()
goose1.name = 'White'
goose1.weight = 3  # kg

cow0 = Cow()
cow0.name = "Manka"
cow0.weight = 720  # kg

sheep0 = Sheep()
sheep0.name = 'Lamb'
sheep0.weight = 70  # kg

sheep1 = Sheep()
sheep1.name = 'Curly'
sheep1.weight = 80  # kg

chicken0 = Chicken()
chicken0.name = 'Ko_ko'
chicken0.weight = 2  # kg

chicken1 = Chicken()
chicken1.name = 'Kukareku'
chicken1.weight = 3  # kg

goat0 = Goat()
goat0.name = 'Hooves'
goat0.weight = 50  # kg

goat1 = Goat()
goat1.name = 'Horns'
goat1.weight = 70  # kg

duck0 = Duck()
duck0.name = 'Mallard'
duck0.weight = 1  # kg

joe_farm = {goose0, goose1, cow0, sheep0, sheep1, chicken0, chicken1, goat0, goat1, duck0}






