# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 3 - Mejorando las imágenes
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow, noise
import cv2
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------
# Escribe tu código aquí:

# Actividad 0: Recordar como leer y mostrar imagenes
img = cv2.imread('./img/7.jpg')
imshow('Foto', img)


# Actividad 1: Ruido
ruido = noise(img)
imshow('Ruido', ruido)


# Actividad 2: Desenfoque a imagen
kernel = np.ones((15, 15), np.float32) / (15*15)
desenfoque = cv2.filter2D(img, -1, kernel)
imshow('Desenfoque', desenfoque)


# Actividad 3: Enfoque
kernel = -1 * np.ones((5, 5), np.float32)
kernel[2, 2] = 25
enfoque = cv2.filter2D(desenfoque, -1, kernel)
imshow('Enfoque', enfoque)

# Actividad 4: brillo y contraste
contraste = 2.0  # Menor a 1 menos contraste mayor a 1 sube el contraste
brillo = -6      # Mantenlo en el rango -255 a 255 de otra forma solo verás negro o blanco
nueva = cv2.convertScaleAbs(img, alpha=contraste, beta=brillo)
imshow('Nueva', nueva)

# Actividad 5 (opcional): viendo diferencias
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.subplot(1, 2, 2)
plt.hist(nueva.ravel(), 256, [0, 256])
plt.show()

# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()