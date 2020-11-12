from random import randint

class Automovil:
    def __init__(self):
        self.placas = ""
        self.modelo = 0
        self.marca = ""
        self.km = 0

    def __str__(self):
        return "{0:6} {1:4} {2:6} {3:4}".format(self.placas, self.modelo, self.marca, self.km)

    def __lt__(self, other):
        return self.placas < other.placas

marcas = ["Audi", "VW", "BMW", "Toyota", "Nissan"]
placas = ["ABC", "JVC", "JZM", "CUC", "UDG"]

autos = []

for i in range(10):
    auto = Automovil()
    auto.placas = placas[randint(0, len(placas)-1)] \
        + str(randint(100, 999))
    auto.modelo = randint(2000, 2021)
    auto.marca = marcas[randint(0, len(marcas)-1)]
    auto.km = randint(0, 1000)

    autos.append(auto)

for auto in autos:
    print(auto)

# autos.sort(reverse=True)
def sort_by_modelo(auto):
    return auto.modelo

# autos.sort(key=sort_by_modelo, reverse=True)
# autos.sort(key=lambda auto: auto.marca, reverse=True)
autos.sort(key=lambda auto: auto.km, reverse=True)
print('\n')

for auto in autos:
    print(auto)

