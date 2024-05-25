# -------------------------------------------------------------------------
# Crack the Code
# Inteligencia Artificial con Python
# Sesion 1 - Detector de rostros
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
import cv2
from camera import getcamera

# -------------------------------------------------------------------------
# Escribe tu código aquí:

# Actividad 0: Instala opencv
# pip install opencv

# Actividad 1: Abre la camara y muestrala en pantalla
'''
# Abrir camara web
camera = getcamera()
cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

# Tomar fotografía
ret, frame = cap.read()

# Mostrar la imagen en pantalla
cv2.imshow('frame', frame)

# Mantener imagen abierta en pantalla
cv2.waitKey(0)
'''

# Actividad 2: Código para que se tomen fotos de forma constante
'''
# Abrir camara web
camera = getcamera()
cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

# Ciclo para tomar fotos de forma continua
while True:
    # Tomar fotografía
    ret, frame = cap.read()

    # Comprobar que exista una imagen
    if not ret:
        break

    # Mostrar la imagen en pantalla
    cv2.imshow('frame', frame)

    # Espera a que toques una tecla para cerrar la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

# Actividad 3 (sesion 2): Agrega el detector de rostros

# Abrir camara web
camera = getcamera()
cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

# Carga el archivo para utilizar el detector de rostros
faceClassif = cv2.CascadeClassifier("rostros.xml")

# Ciclo para tomar fotos de forma continua
while True:
    # Tomar fotografía
    ret, frame = cap.read()

    # Comprobar que exista una imagen
    if not ret:
        break
    # Crea una imagen en escala de grises a partir de la foto
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Utiliza el detector en la imagen de escala de grises
    faces = faceClassif.detectMultiScale(gray,
                                            scaleFactor=1.1,
                                            minNeighbors=5,
                                            minSize=(120, 120),
                                            maxSize=(1000, 1000))

    # Dibuja un rectángulo cuando se detecta un rostro
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    # Mostrar la imagen en pantalla
    cv2.imshow('frame', frame)

    # Espera a que toques una tecla para cerrar la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --------------------------------------------------------------------------
# Cierra la cámara y las ventanas - no borres estas lineas
# Deja estas lineas hasta abajo
cv2.destroyAllWindows()
cap.release()
