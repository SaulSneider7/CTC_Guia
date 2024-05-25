class Perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.ladrar = "Guau"

    def sentarse(self):
        print(self.nombre,"se ha sentado.")

    def darMano(self):
        print(self.nombre,"levanta la pata izquierda.")

    def hambre(self):
        print(self.nombre, "tiene hambre y dice", self.ladrar)

    def pasear(self, cantidad):
        print("A mi perro", self.nombre,"lo saco a pasear", cantidad, "veces al día")

miPerro = Perro("Atena", 1)

tuPerro = Perro("Loki", 3)

elPerro = Perro("Scooby", 7)

print("Los perros que están en el parque son:", miPerro.nombre, tuPerro.nombre, elPerro.nombre)

tuPerro.hambre()
elPerro.darMano()
