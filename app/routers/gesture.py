# app/routers/gestures.py

from fastapi import APIRouter, File, UploadFile
import cv2
import numpy as np  # Importar numpy aquí
from app.services.gesture_recognition import recognize_gesture

router = APIRouter()

@router.post("/recognize-gesture/")
async def recognize_gesture_endpoint(file: UploadFile = File(...)):
    # Leer el archivo de imagen enviado
    contents = await file.read()
    
    # Convertir a un array de NumPy
    nparr = np.fromstring(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Llamar a la función de reconocimiento de gestos
    gesture = recognize_gesture(frame)
    
    return {"recognized_gesture": gesture}
