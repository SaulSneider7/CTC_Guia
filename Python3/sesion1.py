"""
import, variables, while,for,if,operador,llamar a codigos ya hechos(funciones),booleanas,inicializar array, colores
"""
#print("hola a todos!")
#mensaje = "hola amigos!"
#print(mensaje)
#ancho = 1280
#print(ancho)
#alto = 720
#print(alto)
#tam = ancho,alto
#print(tam)

#existe = True
#noexiste = False

"""
n = 0
while n < 5:
	n = n+1
	print(n)
"""
#preguntar: porque sale 5?
"""
funciona = True
while funciona == True:
	print("hola")
"""
#preguntar: porque nunca para?
"""
for i in range(0,5):
	print(i)
"""
#explicar sobre range y for
"""
paises = ["chile", "argentina", "perú"]
for i in paises:
	print(i)
"""
#explicar sobre array simple
"""
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

"""
#dibujos
"""
numeros = []
for i in range(0,5):
	numeros = numeros + [i]
print(numeros)
"""
#explicar como añadir datos en un array vacio
"""
c=1
if c ==1:
	print("Es 1 amigo")
"""
#explicar condicional simple
"""
a = 3 #5
if a == 5:
	print("es el número 5")
else:
	print("no es 5")
"""
#explicar sobre condiciones

#negro = (0,0,0)

"""
def saludo():
	print("Eso es todo amigos!")

saludo()
"""
#explicar sobre funcion simple
"""
def suma(num1,num2):
	resultado = num1+num2
	print(resultado)

suma(4,5)
"""
#funcion que recibe parametros para realizar su trabajo


"""
class Persona:
	def __init__(self, nombre, edad):
		self.name = nombre #mencionar que podria ser self.nombre tambien
		self.years = edad #mencionar que podria ser self.edad tambien

yo = Persona("Pluti", 5)
print(yo.name)
print(yo.years)
"""
"""
Las clases es la forma de generar objetos, POO es programación orientada a objetos, si quieres usar este paradigma tienes que pensar en objetos y clases.
un clase define un tipo de objeto, cuando lo llamas estas creando una instancia de esa clase, cuando quieres que algo suceda llamas a ese objeto y le indicas que lo haga.
__init__ es el constructor de tu clase en el creas una nueva instancia de la clase, por ejemplo
"""