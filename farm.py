class Animal:
    status_hungry = 'хочет есть'
    status_full = "ощущает сытость"
    animal_status = status_hungry

    animal_type = None
    animal_sound = None
    animal_name = None
    animal_weight = 0


    def __init__(self, name, weight):
        self.animal_name = name
        self.animal_weight = weight

    def animal_start(self):
        """Начинаем взаимодействовать с животным"""
        pass

    def get_animal_type(self):
        """Задаем тип животного"""
        return self.animal_type

    def get_animal_status(self):
        """Задаем состояние животного (голоден/сыт)"""
        return self.animal_status



class Egg(Animal):
    """Дающие яйца"""
    egg_status_full = 'Яйца не собраны'
    egg_status_empty = 'гнездо пустое'
    egg_status = egg_status_full



class Milk(Animal):
    """Дающие молоко"""
    milk_status_full = 'вымя, полное молока'
    milk_status_empty = 'вымя пустое'
    milk_status = milk_status_full



class Wool(Animal):
    """Дающие шерсть"""
    hair_style_shaggy = 'повышенная лохматость'
    hair_style_bald = 'Брюс Уиллис'
    hair_style = hair_style_shaggy



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
        print(f'Заглядываем в гнездо. {self.egg_status}. Забираем яйца...')
        self.egg_status = self.egg_status_empty
        print(f'Теперь {self.egg_status}. Пока, {self.animal_name}')
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
    def animal_start(self):
        """
        Взаимодействие с овцой
        """
        print('== == == == == == == ==')
        print(f'Подходим к обитателю фермы по имени {self.animal_name}.')
        print(f'{self.animal_name} - это {self.animal_class}.')
        print(f'Увидев нас, {self.animal_name} начинает кричать "{self.animal_sound}".')
        print(f'Видимо {self.animal_name} {self.animal_status}. Кормим питомца...')
        self.animal_status = self.status_full
        print(f'Ну вот, теперь {self.animal_name} {self.animal_status}.')
        print(f'Что-то у {self.animal_name} {self.hair_style_shaggy}. Видимо, пора сходить к барберу..))')
        self.hair_style = self.hair_style_bald
        print(f'Отлично! Прическа теперь как у {self.hair_style}а. Пока, {self.animal_name}!')
        print('== == == == == == == ==')
        return self.animal_status

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
        print(f'Заглядываем в гнездо. {self.egg_status}. Забираем яйца...')
        self.egg_status = self.egg_status_empty
        print(f'Теперь {self.egg_status}. Пока, {self.animal_name}!')
        print('== == == == == == == ==')
        return self.animal_status

class Goat(Milk):
    animal_sound = "Меее-е-е-е"
    animal_class = "коза"
    def animal_start(self):
        """
        Взаимодействие с козой
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

class Duck(Egg):
    animal_sound = "Кря-кря"
    animal_class = "утка"
    def animal_start(self):
        """
        Взаимодействие с уткой
        """
        print('== == == == == == == ==')
        print(f'Подходим к обитателю фермы по имени {self.animal_name}.')
        print(f'{self.animal_name} - это {self.animal_class}.')
        print(f'Увидев нас, {self.animal_name} начинает кричать "{self.animal_sound}".')
        print(f'Видимо {self.animal_name} {self.animal_status}. Кормим питомца...')
        self.animal_status = self.status_full
        print(f'Ну вот, теперь {self.animal_name} {self.animal_status}')
        print(f'Заглядываем в гнездо. {self.egg_status}. Забираем яйца...')
        self.egg_status = self.egg_status_empty
        print(f'Теперь {self.egg_status}. Пока, {self.animal_name}!')
        print('== == == == == == == ==')
        return self.animal_status


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

def heavyweight():
    """Вычисляем вес и имя жирдяя и общий вес всей фермы"""
    heavy_animal_name = None
    max_weight = 0
    all_farm_weight = 0

    for item in joe_farm:
        all_farm_weight += item.animal_weight
        if item.animal_weight > max_weight:
            max_weight = item.animal_weight
            heavy_animal_name = item.animal_name
    return f'Общий вес животных на ферме {all_farm_weight} кг. Самое тяжелое животное - {heavy_animal_name} с весом' \
           f' {max_weight} кг'

while True:
    cmd = input('Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных. К кому'
                    ' подойдем? \n'
                    '1 или 2 - гуси\n3 - корова\n4 или 5 - овцы\n6 или 7 - курицы\n8 или 9 - козы\n10 - утка\nА может '
                'желаете узнать самое тяжелое животное и общий вес живности на ферме (введите "0")\n'
                'Ваш выбор? :  ')
    if cmd == "1":
        goose0.animal_start()
    elif cmd == "2":
        goose1.animal_start()
    elif cmd == "3":
        cow0.animal_start()
    elif cmd == "4":
        sheep0.animal_start()
    elif cmd == "5":
        sheep1.animal_start()
    elif cmd == "6":
        chicken0.animal_start()
    elif cmd == "7":
        chicken1.animal_start()
    elif cmd == "8":
        goat0.animal_start()
    elif cmd == "9":
        goat1.animal_start()
    elif cmd == "10":
        duck0.animal_start()
    elif cmd == "0":
        print('== == == == == == == ==')
        print(heavyweight())
        print('== == == == == == == ==')
    else:
        print('Таких животных нет на ферме, сорь. Может попробуем еще раз?')
        print('== == == == == == == ==')