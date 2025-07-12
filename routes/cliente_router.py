from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from business_layer.work_of_unity import UnitOfWok
from dtos.ClienteDto import ClienteDto
from dtos.IdDto import IdDto, MensajeDto

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
async def obtener_todos(
    pagina_actual: int = 1, registros_por_pagina: int = 10, filtro: str = ""
):
    paginado = uow.cliente.obtener_todos(pagina_actual, registros_por_pagina, filtro)
    dtos = _to_list(paginado.lista)

    return JSONResponse(
        content=dtos,
        headers={
            "total": str(paginado.total),
            "total_filtrados": str(paginado.total_filtrados),
        },
    )

@cliente_router.get(
    "/{encodedkey}",
    summary="Obtener cliente por clave",
    response_model=ClienteDto,
)
async def obtener_por_clave(encodedkey: str):
    cliente = uow.cliente.obtener_por_clave(encodedkey)
    if cliente is None:
        mensaje_dto = MensajeDto(
            id=0,
            encodedkey=encodedkey,
            fecha=str(datetime.now().isoformat()),
            mensaje="Cliente no encontrado",
        )
        return JSONResponse(status_code=404, content=mensaje_dto.to_dict()  )

    return JSONResponse(content=cliente.to_dict())
