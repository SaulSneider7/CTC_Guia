"""
print("S")

a = ord("j")

print(a)


b = chr(100)
print(b)


palabra = "hola"
cambio = 5
palabraFinal = ""

for letra in palabra:
    nuevo = ord(letra) + cambio
    letraNueva = chr(nuevo)
    palabraFinal += letraNueva

print(palabraFinal)


letra = "x"
cambio = 3
nuevo = ord(letra) + cambio

print(chr(nuevo))


"""
def cifrar():
    # definir el cambio de cada letra

    texto = input("Ingrese el texto a cifrar: ")

    cambio = int(input("Ingrese el cambio que le quiere dar: "))
    
    texto_final = ""

    for c in texto:

        # comprobar si la letra es mayúscula:
        if c.isupper():

            # encontrar la posición en el abecedario.
            c_index = ord(c) - ord("A")

            # hacer el cambio en la letra
            new_index = (c_index + cambio) % 26

            # convertir el nuevo número a letra
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # añadirlo al texto final
            texto_final = texto_final + new_character


        elif c.islower():  #comprobar si es minúscula

            # encontrar la posición en el abecedario.
            c_index = ord(c) - ord("a")

            # hacer el cambio en la letra
            new_index = (c_index + cambio) % 26

            # convertir el nuevo número a letra
            new_unicode = new_index + ord("a")

            new_character = chr(new_unicode)

            # añadirlo al texto final
            texto_final = texto_final + new_character

        elif c.isdigit():

            # si es un dígito, cambiar su valor
            c_new = (int(c) + cambio) % 10

            texto_final += str(c_new)

        elif c==" ":
            texto_final = texto_final + " "

    print("Texto a cifrar:", texto)

    print("Texto descifrado:", texto_final)

def descifrar():
    texto = input("Ingrese el texto a descifrar: ")

    cambio = int(input("Ingrese el cambio que quiere revertir: "))

    texto_final = ""

    for c in texto:

        #comprobar si la letra es mayúscula:
        if c.isupper():

            #encontrar la posición en el abecedario.
            c_index = ord(c) - ord("A")

            #deshacer el cambio hecho en la letra
            new_index = (c_index - cambio) % 26

            #convertir el nuevo número a letra
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            #añadirlo al texto final
            texto_final = texto_final + new_character


        elif c.islower():   #Comprobar si la letra es minúscula

            # encontrar la posición en el abecedario.
            c_index = ord(c) - ord("a")

            # deshacer el cambio hecho en la letra
            new_index = (c_index - cambio) % 26

            # convertir el nuevo número a letra
            new_unicode = new_index + ord("a")

            new_character = chr(new_unicode)

            # añadirlo al texto final
            texto_final = texto_final + new_character

        elif c.isdigit():

            # si es un número, regresar a su valor original
            c_new = (int(c) - cambio) % 10

            texto_final += str(c_new)

        elif c==" ":
            texto_final = texto_final + " "

    print("Texto cifrado:",texto)

    print("Texto descifrado:",texto_final)

descifrar()


