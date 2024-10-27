from fastapi import FastAPI, File, UploadFile 
import uvicorn
import numpy as np
import cv2
import mediapipe as mp

app = FastAPI()

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Definición de los gestos (abecedario y más)
GESTURES = {
    "A": "Mano en puño con el pulgar sobre los dedos.",
    "B": "Palma hacia adelante, dedos juntos y estirados.",
    "C": "Mano en forma de 'C'.",
    "D": "Mano en forma de 'D' con el dedo índice hacia arriba.",
    "E": "Mano en puño con los dedos doblados hacia la palma.",
    "F": "Pulgar y dedo índice en forma de círculo, representación de 'Fiorella'.",
    "G": "Pulgar e índice señalando hacia afuera, como una pistola.",
    "H": "Índice y medio juntos hacia el frente.",
    "I": "Mano en puño con el meñique estirado hacia arriba.",
    "J": "Forma una 'J' con el meñique.",
    "K": "Mano abierta con el pulgar levantado.",
    "L": "Mano en forma de 'L'.",
    "M": "Mano en puño con el pulgar sobre los dedos.",
    "N": "Mano en puño con el pulgar apuntando hacia afuera.",
    "O": "Mano en forma de círculo.",
    "P": "Mano en forma de 'P'.",
    "Q": "Mano en forma de 'Q'.",
    "R": "Mano en forma de 'R'.",
    "S": "Mano en puño.",
    "T": "Mano en puño con el pulgar entre los dedos.",
    "U": "Mano en forma de 'U'.",
    "V": "Mano en forma de 'V'.",
    "W": "Mano en forma de 'W'.",
    "X": "Mano en forma de 'X'.",
    "Y": "Mano en forma de 'Y'.",
    "Z": "Mano en forma de 'Z'.",
}

# Definición de preguntas
QUESTIONS = {
    "D": "¿Tienes dirección?",
    "W": "¿Tienes WhatsApp?",
    "V": "¿Dónde vives?",
    "C": "¡Con mucho gusto conocerte?",
    "N": "¿Cómo te llamas?",
    "B": "¿Cuándo es tu cumpleaños?",
}

# Definición de expresiones faciales
FACIAL_EXPRESSIONS = {
    "S": "Sería.",
    "M": "Molesta.",
    "H": "Feliz.",
    "Su": "Sorprendida.",
    "Tr": "Triste.",
    "En": "Enojada.",
}

@app.post("/recognize-gesture/")
async def recognize_gesture(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convertir la imagen a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture = "Unknown"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Aquí puedes agregar la lógica de detección de gestos
            gesture = recognize_sign(hand_landmarks)  # Llama a la función de reconocimiento
            
    # Aquí generamos la respuesta con base en el gesto reconocido
    response = {
        "gesture": gesture,
        "description": GESTURES.get(gesture, "Gesto desconocido"),
        "question": QUESTIONS.get(gesture, ""),
        "facial_expression": np.random.choice(list(FACIAL_EXPRESSIONS.values())),  # Escoge una expresión al azar
    }
    return response

def recognize_sign(hand_landmarks):
    # Aquí puedes implementar la lógica para reconocer el gesto basado en los landmarks
    # Ejemplo de detección para el gesto 'F'
    # Agregar lógica para cada gesto
    # Aquí simulamos que detectamos el gesto 'F'
    return "F"  # Simulación, reemplaza con lógica real

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
