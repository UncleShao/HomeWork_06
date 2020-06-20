from pprint import pprint

class Animals:
    name = 'Name'
    weight = 0
    condition = 'hungry'

    def __init__(self):
        self.feed = 'fed'



goose0 = Animals()
goose0.name = 'Gray'
goose0.weight = 4 #kg

goose1 = Animals()
goose1.name = 'White'
goose1.weight = 3 #kg


Cow = Animals()

class Sheep:
    pass

class Chicken:
    pass

class Goat:
    pass

class Duck:
    pass

pprint(Animals.__dict__)
print(goose0.__dict__)
print(goose1.__dict__)




