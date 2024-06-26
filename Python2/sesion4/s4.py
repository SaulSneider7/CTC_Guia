open("Mi archivo.txt")

t = open("Mi archivo.txt", "w")

t.close()


with open("Mi archivo.txt", "w", encoding="utf-8") as t:
    t.write("Este es mi primer archivo \n")
    t.write("Fin.\n")


# lista1=[3, 1, "Hola", "Fin"]

# with open("Mi archivo.txt", "w", encoding="utf-8") as t:
#     t.write(str(lista1[0]))
#     t.write(str(lista1[1])+"\n")
#     t.write(str(lista1[2])+"\n")
#     t.write(str(lista1[3])+"\n")



# with open("Mi archivo.txt", "a", encoding="utf-8") as t:
#     t.write("Vamos a continuar escribiendo\n")
#     t.write("Podemos añadir comentarios al final\n")


# PARTE 2
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# with open("Nombres.txt", "w", encoding="utf-8") as t:
#     t.write("Nombre: "+ nombre + "\n")
#     t.write("Edad: "+ str(nombre) + "\n")
