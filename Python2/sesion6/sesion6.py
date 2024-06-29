print("Sesion 6")

import turtle

#creamos el lapiz
t = turtle.Turtle()
t.forward(10)   #Adelante
t.backward(10)  #Atras

t.left(30)      #Izquierda
t.right(30)     #Derecha

turtle.setup(600, 600) 
turtle.bgcolor("white")
turtle.title("Mi Dibujo 1")


#Dibujamos un circulo
t.circle(100)

#dibujamos un cuadrado
for x in range (4):
    t.forward(100)
    t.left(90)

#creo un nuevo lapiz
t2 = turtle.Turtle()
turtle.bgcolor("black")

#lista de colores
listaColores = ["red", "magenta", "blue", "cyan", "green", "yellow", "orange", "purple", "white"]


#Dibujamos circulos con diferentes colores
for x in range(8):
    for colores in listaColores:
        t2.pencolor(colores)
        t2.circle(100)
        t2.left(50)


turtle.done()