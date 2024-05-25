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



class Cachorro(Perro):

    def __init__(self, nombre, edad, energia):
        super().__init__(nombre, edad)
        self.energia = energia

    def jugar(self):
        nivelActividad = self.energia/self.edad
        print("El cachorro estará jugando", nivelActividad, "horas.")