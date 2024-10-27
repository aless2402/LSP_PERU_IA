from fastapi import FastAPI
from app.database.db import Base, engine
from app.routers import gesture, auth, websocket

app = FastAPI(title="LSP IA Reconocimiento")

# Iniciar la base de datos y crear las tablas necesarias
Base.metadata.create_all(bind=engine)

# Rutas
app.include_router(gesture.router)
app.include_router(auth.router)
app.include_router(websocket.router)

# Endpoint básico de prueba
@app.get("/")
async def root():
    return {"message": "Bienvenido al Sistema de Reconocimiento de LSP CON IA"}
