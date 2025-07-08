from datetime import datetime
import uuid
from fastapi import FastAPI

from dtos.IdDto import MensajeDto
from routes.cliente_router import cliente_router

app = FastAPI(
    title="Banco del Bienestar",
    description="Api de clientes y depositos",
)


@app.get("/saludar", response_model=MensajeDto, summary="Hola mundo", tags=["Hola mundo"])
async def greet():
    mensaje = {
        "fecha": str(datetime.now().isoformat()),
        "mensaje": "Hola mundo",
        "encodedkey": str(uuid.uuid4()),
    }

    # return MensajeDto(
    #     encodedkey=str( uuid.uuid4()),
    #     fecha=str(datetime.now().isoformat()),
    #     mensaje="Hola mundo"
    # )

    return MensajeDto(**mensaje)

app.include_router(cliente_router, prefix="/api/Clientes", tags=["Clientes"])