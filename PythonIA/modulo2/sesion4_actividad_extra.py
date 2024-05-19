# -------------------------------------------------------------------------
# Crack the Code
# Inteligencia Artificial con Python
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
import cv2
from camera import getcamera

# -------------------------------------------------------------------------
# Escribe tu código aquí:

# Abre la camara
camera = getcamera()
cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

# Si no funciona la camara de la forma anterior intenta con estas funciones
# camera = getcamera()
# cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

# Carga el archivo para utilizar el clasificador de rostros
faceClassif = cv2.CascadeClassifier("rostros.xml")

# Carga el archivo para utilizar el clasificador de ojos
eyeClassif = cv2.CascadeClassifier("ojos.xml")

# Crea dos arreglos para pintar en pantalla
x1 = []
y1 = []

# Utiliza la camara hasta que la tecla q es presionada
while True:
    # Toma una fotografía y la muestra en pantalla
    ret, frame = cap.read()

    # comprobar que exista una imagen
    if not ret:
        break

    # Crea una imagen en escala de grises a partir de la foto
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Utiliza el detector de rostros en la imagen de escala de grises
    faces = faceClassif.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(120, 120),
                                         maxSize=(1000, 1000))

    # Utiliza el detector de ojos en la imagen de escala de grises
    eyes = eyeClassif.detectMultiScale(gray,
                                       scaleFactor=1.1,
                                       minNeighbors=10,
                                       minSize=(50, 50),
                                       maxSize=(300, 300))

    # Dibuja un rectángulo cuando se detecta un rostro
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Dibuja un rectángulo cuando se detectan los ojos
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

        # Agrega las coordenadas de los ojos a los arreglos
        x1.append(x + int(w / 2))
        y1.append(y + int(h / 2))

    # Dibuja circulos en las posiciones guardadas
    for j in range(len(x1)):
        cv2.circle(frame, (x1[j], y1[j]), 4, (255, 155, 100), 5)

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
