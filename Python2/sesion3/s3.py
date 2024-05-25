import os


#print(os.getlogin())  #El nombre de usuario que inició sesión en la PC.

#print(os.getcwd()) #La dirección de la carpeta actual donde nos encontramos.

#print(os.listdir("C:/Users/Cracker/PycharmProjects"))  #Lista de elementos presente en la carpeta

#os.mkdir("Carpeta 1")    #Crear una nueva carpeta en dicha dirección.

#os.rename("Carpeta 1", "Carpeta 123")  #Cambiar el nombre a una carpeta que se encuentra en dicha dirección.

#os.rmdir("C:/Users/Cracker/Desktop/1234")  #Eliminar una carpeta que se encuentra en dicha dirección.

#os.chdir("C:/Users/Cracker/Desktop") #Moverse a otro directorio o ruta específico.

#os.startfile("Captura Python 1.png") #Abrir un archivo o programa que se encuentra en la ruta donde estamos.

#Mini Proyecto (Pueden escogerse otros programas)
lista = ["Chrome", "Internet Explorer", "Edge"]

for x in range(3):
    print(x+1, lista[x])

eleccion = int(input("Escoja una opción: "))

if eleccion == 1:
    os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")

elif eleccion == 2:
    os.startfile("C:/Program Files (x86)/Internet Explorer/iexplore.exe")

elif eleccion ==3:
    os.startfile("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")



