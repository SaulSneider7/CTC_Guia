# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 1 - Introducción a las imágenes digitales
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:


# Actividad 0: Set up
# 1) Verifica que todos tus alumnos tengan pycharm instalado
# 2) Crea un nuevo proyecto con venv en pycharm
# 3) Verifica que todos tus alumnos tengan python instalado
# NOTA: Si no lo tienen la descarga empezará en automático al crear un nuevo proyecto.
# 4) Haz que tus alumnos copien la plantilla en su proyecto


# Actividad 1: instalar biblioteca de OpenCV
# Abre la terminal y escribe lo siguiente:
# pip install opencv-python


# Actividad 2: Leer imágenes y mostrarlas en pantalla
img = cv2.imread('./img/14.jpg')
imshow('Foto', img)


# Actividad 3: Crear imágenes negra, blanca y gris
negro = np.zeros(img.shape, np.uint8)
imshow('Negro', negro)

blanco = 255 * np.ones(img.shape, np.uint8)
imshow('Blanco', blanco)

gris = 150 * np.ones(img.shape, np.uint8)  # Puedes cambiar el numero entre 0 y 255
imshow('Gris', gris)


# Actividad 4: Ver los diferentes colores de una imagen
# No hace falta hacer todos solo con un color es suficiente
azul = img[:, :, 0]
imshow('Azul', azul)

verde = img[:, :, 1]
imshow('Verde', verde)

rojo = img[:, :, 2]
imshow('Rojo', rojo)


# Actividad 5 (opcional): Ver los diferentes colores de una imagen parte 2
# Durante la clase no vuelvas a rescribirlo solo modifica la actividad anterior
# NOTA: no es necesario hacerlas todas, con 1 es suficiente (dependiendo del tiempo)
azul = np.zeros(img.shape, np.uint8)
azul[:, :, 0] = img[:, :, 0]
imshow('Azul', azul)

verde = np.zeros(img.shape, np.uint8)
verde[:, :, 1] = img[:, :, 1]
imshow('Verde', verde)

rojo = np.zeros(img.shape, np.uint8)
rojo[:, :, 2] = img[:, :, 2]
imshow('Rojo', rojo)


# Actividad 6: Guardar imágenes
# NOTA: no es necesario hacerlas todas, con 2 es suficiente
cv2.imwrite('./out/blanco.jpg', blanco)
cv2.imwrite('./out/negro.jpg', negro)
cv2.imwrite('./out/gris.jpg', gris)
cv2.imwrite('./out/azul.jpg', azul)
cv2.imwrite('./out/rojo.jpg', rojo)
cv2.imwrite('./out/verde.jpg', verde)

# Actividad 7 (opcional): pide a tus alumnos que cambien la imagen (Actividad 2).
# NOTA: La imagen 17 es interesante pues tiene muchos colores.

# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tip: en cualquier momento puedes anotar cv2.destroyAllWindows()
# para no ver tantas ventanas. Como alternativa también le puedes
# pedir a los niños que comenten algunas lineas