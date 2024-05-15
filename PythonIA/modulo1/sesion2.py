# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 2 - Imágenes en blanco y negro
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------
# Escribe tu código aquí:

# Actividad 0: Recordar como leer y mostrar imagenes
img = cv2.imread('./img/14.jpg')
imshow('Foto', img)


# Actividad 1: transformar la imagen a escala de grises
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imshow('Grises', grises)


# Actividad 2: histograma
# Instalar nueva biblioteca para ver graficas. Escribe en la terminal:
# pip install matplotlib
plt.hist(grises.ravel(), 256, [0, 256])
plt.show()


# Actividad 3: Imagen binaria
# Esta actividad funciona mejor con las imagenes 3, 6, 14 y 22
_, binaria = cv2.threshold(grises, 86, 255, cv2.THRESH_BINARY)  # Modifica el segundo parámetro
imshow('Binaria', binaria)


# Actividad 4: Complemento de imagen
complemento = cv2.bitwise_not(binaria)
imshow('Complemento', complemento)


# Actividad 5 (opcional): Ver tamaños de las imagenes
print("Foto:")
print(img.shape)
print("Grises:")
print(grises.shape)
print("Binaria:")
print(binaria.shape)


# Actividad 6: Operaciones de dilatación, erosión, apertura y cerradura
# NOTA: no hace falta verlas todas,
# el objetivo es quitar el ruido de la imagen y puedes usarlas en cascada
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(binaria, kernel)
imshow('Erosion', erosion)

dilatacion = cv2.dilate(erosion, kernel)
imshow('Dilatacion', dilatacion)

apertura = cv2.morphologyEx(dilatacion, cv2.MORPH_OPEN, kernel)
imshow('Apertura', apertura)

cerradura = cv2.morphologyEx(apertura, cv2.MORPH_CLOSE, kernel)
imshow('Cerradura', cerradura)


# Actividad 7: Separando un objeto de una imagen (máscaras)
tortuga = np.zeros(img.shape, np.uint8)
for i in range(3):
    tortuga[:, :, i] = cv2.bitwise_and(img[:, :, i], erosion)
imshow('Tortuga', tortuga)


# Actividad 8 (opcional): Agregar fondo a imagen
fondo = cv2.imread("./img/fondo.jpg")
for i in range(3):
    fondo[:, :, i] = cv2.bitwise_and(fondo[:, :, i], cv2.bitwise_not(erosion))
imshow('Tortuga', tortuga)
tortuga += fondo
imshow('Tortuga2', tortuga)

# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()