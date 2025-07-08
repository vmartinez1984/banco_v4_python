from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from business_layer.work_of_unity import UnitOfWok
from dtos.ClienteDto import ClienteDto

cliente_router = APIRouter()
uow = UnitOfWok()


def _to_list(dtos: List[ClienteDto]) -> List:
    lista = []
    for dto in dtos:
        lista.append(dto.to_dict())

    return lista


@cliente_router.get(
    "/", summary="Obtener todos los clientes", response_model=List[ClienteDto]
)
async def obtener_todos():
    dtos = uow.cliente.obtener_todos()    
    dtos = _to_list(dtos)

    return JSONResponse(content=dtos)
