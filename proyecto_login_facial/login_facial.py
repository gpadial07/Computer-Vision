
import cv2
import os



# CARGAR



cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade_path)
if detector.empty():
    print("Error cargando el detector facial")
    exit()



# INICIAR



camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("No se pudo abrir la cámara")
    exit()
print("Sistema iniciado")
print("Presiona Q para salir")



# LOGIN



while True:
    ret, frame = camara.read()
    if not ret:
        print("Error leyendo cámara")
        break
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = detector.detectMultiScale(
        gris,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    acceso = False

    for (x, y, w, h) in rostros:
        acceso = True
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )
        cv2.putText(
            frame,
            "ROSTRO DETECTADO",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )
    if acceso:
        cv2.putText(
            frame,
            "ACCESO AUTORIZADO",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )
    else:
        cv2.putText(
            frame,
            "ACCESO DENEGADO",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )
    cv2.imshow("Login Facial", frame)
    tecla = cv2.waitKey(1)
    if tecla == ord("q"):
        break



# CERRAR



camara.release()
cv2.destroyAllWindows()
