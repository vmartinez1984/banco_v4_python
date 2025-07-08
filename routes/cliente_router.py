from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from business_layer.work_of_unity import WorkOfUnity
from dtos.ClienteDto import ClienteDto

cliente_router = APIRouter()
wou = WorkOfUnity()

@cliente_router.get(
        "/", 
        summary="Obtener todos los clientes",
        response_model=List[ClienteDto]
    )
async def obtener_todos():
    dtos = wou.cliente.obtener_todos()
    return JSONResponse(content={"mensaje": "Hola mundo"})