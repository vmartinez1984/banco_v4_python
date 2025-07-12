from dtos.AhorroDto import AhorroDto, MovimientoDto, MovimientoDtoIn
from dtos.IdDto import IdDto
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import List
from business_layer.work_of_unity import UnitOfWok


ahorro_router = APIRouter()
uow = UnitOfWok()

@ahorro_router.get("/clientes/{encodedkey}", summary="Obtener ahorros por cliente", response_model=List[AhorroDto])
async def obtener_ahorros_por_cliente(encodedkey: str):
    """
    Obtiene todos los ahorros de un cliente específico.
    """
    ahorros = uow.ahorro.obtener_ahorros_por_cliente(encodedkey)
    if not ahorros:
        mensaje_dto = {
            "id": 0,
            "encodedkey": encodedkey,
            "fecha": str(datetime.now().isoformat()),
            "mensaje": "No se encontraron ahorros para el cliente."
        }
        return JSONResponse(status_code=404, content=mensaje_dto)

    return JSONResponse(content=[ahorro.to_dict() for ahorro in ahorros])

@ahorro_router.get("/{encodedkey}/movimientos", summary="Obtener movimientos de ahorro por clave", response_model=List[AhorroDto])
async def obtener_movimientos_por_clave(encodedkey: str)->List[MovimientoDto]:
    """Obtiene todos los movimientos de ahorro de un específico.

    Args:
        encodedkey (str): ahorro encoded key o id.

    Returns:
        List[MovimientoDto]: movimientos de ahorro.
    """
    ahorro = uow.ahorro.obtener_ahorro_por_clave(encodedkey)
    if not ahorro:
        mensaje_dto = {
            "id": 0,
            "encodedkey": encodedkey,
            "fecha": str(datetime.now().isoformat()),
            "mensaje": "No se encontro el ahorro."
        }
        return JSONResponse(status_code=404, content=mensaje_dto)
    movimientos = uow.ahorro.obtener_movimientos_por_clave(encodedkey)

    return JSONResponse(content=[movimiento.to_dict() for movimiento in movimientos])


@ahorro_router.get(
    "/movimientos/{encodedkey}", 
    summary="Obtener movimiento por clave", 
    response_model=MovimientoDto
)
async def obtener_movimiento_por_clave(encodedkey: str):
    """
    Obtiene un movimiento específico por su clave.

    Args:
        encodedkey (str): Clave del movimiento.

    Returns:
        MovimientoDto: DTO del movimiento.
    """
    movimiento = uow.ahorro.obtener_movimiento_por_clave(encodedkey)
    if not movimiento:
        mensaje_dto = {
            "id": 0,
            "encodedkey": encodedkey,
            "fecha": str(datetime.now().isoformat()),
            "mensaje": "Movimiento no encontrado."
        }
        return JSONResponse(status_code=404, content=mensaje_dto)

    return JSONResponse(content=movimiento.to_dict())

@ahorro_router.post("/{encodedkey}/Depositos", summary="Hacer deposito", response_model=IdDto)
async def hacer_deposito(encodedkey: str,deposito: MovimientoDtoIn):
    """
    Hace un deposito a un ahorro específico.

    Args:
        encodedkey (str): Clave del ahorro.
        deposito (MovimientoDtoIn): Datos del deposito.

    Returns:
        IdDto: DTO con el id del movimiento realizado.
    """
    if not deposito.referencia:
        movimiento = uow.ahorro.obtener_movimiento_por_referencia(deposito.referencia)
        if movimiento:
            mensaje_dto = {
                "id": 0,
                "encodedkey": encodedkey,
                "fecha": str(datetime.now().isoformat()),
                "mensaje": f"Ya existe un movimiento con la referencia {deposito.referencia}."
            }
            return JSONResponse(status_code=400, content=mensaje_dto)
  
    iddto = uow.ahorro.hacer_deposito(encodedkey, deposito)

    return JSONResponse(content=iddto.to_dict(), status_code=201)

@ahorro_router.post("/{encodedkey}/Retiros", summary="Hacer retiro", response_model=IdDto)
async def hacer_retiro(encodedkey: str, retiro: MovimientoDtoIn):
    """
    Hace un retiro de un ahorro específico.

    Args:
        encodedkey (str): Clave del ahorro.
        retiro (MovimientoDtoIn): Datos del retiro.

    Returns:
        IdDto: DTO con el id del movimiento realizado.
    """
    if not retiro.referencia:
        movimiento = uow.ahorro.obtener_movimiento_por_referencia(retiro.referencia)
        if movimiento:
            mensaje_dto = {
                "id": 0,
                "encodedkey": encodedkey,
                "fecha": str(datetime.now().isoformat()),
                "mensaje": f"Ya existe un movimiento con la referencia {retiro.referencia}."
            }
            return JSONResponse(status_code=400, content=mensaje_dto)
    
    ahorro = uow.ahorro.obtener_ahorro_por_clave(encodedkey)
    if ahorro.total < retiro.cantidad:
        mensaje_dto = {
            "id": 0,
            "encodedkey": encodedkey,
            "fecha": str(datetime.now().isoformat()),
            "mensaje": f"Saldo insuficiente para realizar el retiro {retiro.cantidad}."
        }
        return JSONResponse(status_code=400, content=mensaje_dto)
    movimiento = uow.ahorro.hacer_retiro(encodedkey, retiro)

    return IdDto(id=movimiento.id, encodedkey=movimiento.encodedkey)