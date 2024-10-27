import cv2
import requests
import speech_recognition as sr

# URL de tu API para el reconocimiento de gestos
url = "http://localhost:8000/recognize-gesture/"

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Captura de video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el frame a JPEG y enviarlo al servidor
    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(url, files={'file': img_encoded.tobytes()})

    # Procesar la respuesta del servidor
    if response.status_code == 200:
        result = response.json()
        gesture = result.get("gesture", "Desconocido")
        description = result.get("description", "")
        question = result.get("question", "")
        facial_expression = result.get("facial_expression", "")

        # Crear un texto para los subtítulos de gestos
        gesture_subtitles = [
            f"Gesto: {gesture}",
            description,
            question if question else "",
            facial_expression if facial_expression else ""
        ]

        # Mostrar los subtítulos de gestos en el marco de video
        y_position = 50  # Posición inicial para los subtítulos
        for line in gesture_subtitles:
            if line:  # Solo mostrar líneas no vacías
                cv2.putText(frame, line, (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
                y_position += 40  # Espaciado entre líneas

    # Reconocimiento de voz
    with sr.Microphone() as source:
        print("Escuchando...")  # Mensaje para indicar que está escuchando
        audio = recognizer.listen(source)

        try:
            # Transcribir la voz a texto
            spoken_text = recognizer.recognize_google(audio, language='es-ES')
            print(f"Texto hablado: {spoken_text}")

            # Mostrar el texto hablado en el marco de video
            cv2.putText(frame, f"Voz: {spoken_text}", (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError as e:
            print(f"Error con el servicio de reconocimiento de voz: {e}")

    # Mostrar el video
    cv2.imshow('Video', frame)

    # Romper el ciclo si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Mensaje final en la consola
print("Cámara cerrada. Gracias por usar el sistema de reconocimiento de señas.")
