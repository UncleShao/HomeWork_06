class Animal:
    status_hungry = 'хочет есть'
    status_full = "ощущает сытость"
    animal_status = status_hungry

    animal_type = None
    animal_sound = None
    animal_name = None
    animal_weight = 0


    def animal_start(self):
        """Начинаем взаимодействовать с животным"""
        pass

    def get_animal_type(self):
        """Задаем тип животного"""
        return self.animal_type

    def get_animal_status(self):
        """Задаем состояние животного (голоден/сыт)"""
        return self.animal_status

    def __init__(self, name, weight):
        self.animal_name = name
        self.animal_weight = weight



class Egg(Animal):
    egg_status_full = 'Яйца не собраны'
    egg_status_empty = 'гнездо пустое'
    laying_hen = egg_status_full
    animal_type = 'Дающие яйца'




class Milk(Animal):
    milk_status_full = 'вымя, полное молока'
    milk_status_empty = 'вымя пустое'
    milk_status = milk_status_full
    animal_type = 'Дающие молоко'

    def milked(self):
        """Доим"""
        self.milk_status = 'empty'


class Wool(Animal):
    hair_style = 'shaggy'
    animal_type = 'Дающие шерсть'

    def cut(self):
        """Стрижем"""
        self.hair_style = 'bald'


class Goose(Egg):
    animal_sound = "Га-га-га"
    animal_class = "гусь"
    def animal_start(self):
        """
        Взаимодействие с гусями
        """
        print('== == == == == == == ==')
        print(f'Подходим к обитателю фермы по имени {self.animal_name}.')
        print(f'{self.animal_name} - это {self.animal_class}.')
        print(f'Увидев нас, {self.animal_name} начинает кричать "{self.animal_sound}".')
        print(f'Видимо {self.animal_name} {self.animal_status}. Кормим питомца...')
        self.animal_status = self.status_full
        print(f'Ну вот, теперь {self.animal_name} {self.animal_status}')
        print(f'Заглядываем в гнездо. {self.laying_hen}. Забираем яйца...')
        self.laying_hen = self.egg_status_empty
        print(f'Теперь {self.laying_hen}. Пока, {self.animal_name}')
        print('== == == == == == == ==')

        return self.animal_status


class Cow(Milk):
    animal_sound = "Мууу-у-у-у"
    animal_class = "корова"
    def animal_start(self):
        """
        Взаимодействие с коровой
        """
        print('== == == == == == == ==')
        print(f'Подходим к обитателю фермы по имени {self.animal_name}.')
        print(f'{self.animal_name} - это {self.animal_class}.')
        print(f'Увидев нас, {self.animal_name} начинает кричать "{self.animal_sound}".')
        print(f'Видимо {self.animal_name} {self.animal_status}. Кормим питомца...')
        self.animal_status = self.status_full
        print(f'Ну вот, теперь {self.animal_name} {self.animal_status}.')
        print(f'Замечаем, что у {self.animal_name} {self.milk_status_full}. Надо срочно ее подоить!')
        self.milk_status = self.milk_status_empty
        print(f'Ого, сколько молока! Теперь {self.milk_status}. Пока, {self.animal_name}!')
        print('== == == == == == == ==')
        return self.animal_status

class Sheep(Wool):
    animal_sound = "Беее-е-е-е"
    animal_class = "овца"


class Chicken(Egg):
    animal_sound = "Ко-ко-ко"
    animal_class = "курица"
    def animal_start(self):
        """
        Взаимодействие с курицей
        """
        print('== == == == == == == ==')
        print(f'Подходим к обитателю фермы по имени {self.animal_name}.')
        print(f'{self.animal_name} - это {self.animal_class}.')
        print(f'Увидев нас, {self.animal_name} начинает кричать "{self.animal_sound}".')
        print(f'Видимо {self.animal_name} {self.animal_status}. Кормим питомца...')
        self.animal_status = self.status_full
        print(f'Ну вот, теперь {self.animal_name} {self.animal_status}')
        print(f'Заглядываем в гнездо. {self.laying_hen}. Забираем яйца...')
        self.laying_hen = self.egg_status_empty
        print(f'Теперь {self.laying_hen}. Пока, {self.animal_name}!')
        print('== == == == == == == ==')
        return self.animal_status

class Goat(Milk):
    animal_sound = "Меее-е-е-е"
    animal_class = "коза"


class Duck(Egg):
    animal_sound = "Кря-кря"
    animal_class = "утка"


goose0 = Goose('Серый', 4)
goose1 = Goose('Белый', 3)
cow0 = Cow('Манька', 720)
sheep0 = Sheep('Барашек', 70)
sheep1 = Sheep('Кудрявый', 80)
chicken0 = Chicken('Коко', 2)
chicken1 = Chicken('Кукареку', 3)
goat0 = Goat('Рога', 50)
goat1 = Goat('Копыта', 70)
duck0 = Duck('Кряква', 1)

joe_farm = [goose0, goose1, cow0, sheep0, sheep1, chicken0, chicken1, goat0, goat1, duck0]


def heavyweight(self):
    heavy_animal_name = None
    max_weight = 0
    all_farm_weight = 0

    for item in self.joe_farm:
        all_farm_weight += item.animal_weight
        if item.animal_weight > max_weight:
            max_weight = item.animal_weight
            heavy_animal_name = item.animal_name
    return f'Общий вес животных на ферме {all_farm_weight} кг. Самое тяжелое животное - {heavy_animal_name} с весом {max_weight} кг'

cow0.animal_start()

