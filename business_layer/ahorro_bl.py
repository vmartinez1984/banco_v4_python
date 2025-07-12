from datetime import datetime
from typing import List
from uuid import uuid4
from dtos.AhorroDto import AhorroDto, MovimientoDto, MovimientoDtoIn
from dtos.IdDto import IdDto
from entities.ahorro_entity import AhorroEntity, MovimientoEntity
from repositories.repository import Respository


class AhorroBl:
    def __init__(self):
        self.repo = Respository()

    def obtener_ahorros_por_cliente(self, encodedkey: str) -> List[AhorroDto]:
        """
        Obtiene todos los ahorros de un cliente específico.
        """
        cliente = self.repo.cliente.obtener_por_clave(encodedkey)
        guid = cliente.otros.get("Guid", None)
        print(guid)
        entities = self.repo.ahorro.obtener_ahorros_por_cliente(guid)
        dtos = [self._obtener_dto(item) for item in entities]

        return dtos

    def obtener_ahorro_por_clave(self, encodedkey: str) -> AhorroDto:
        """
        Obtiene un ahorro específico por su clave.

        Args:
            encodedkey (str): Clave del ahorro.

        Returns:
            AhorroDto: DTO del ahorro.
        """
        entity = self.repo.ahorro.obtener_ahorro_por_clave(encodedkey)
        if entity is None:
            return None

        return self._obtener_dto(entity)

    def obtener_movimientos_por_clave(self, encodedkey: str) -> List[AhorroDto]:
        """
        Obtiene todos los movimientos de ahorro de un específico.

        Args:
            encodedkey (str): ahorro encoded key o id.

        Returns:
            List[AhorroDto]: Lista de movimientos de ahorro.
        """
        entities = self.repo.ahorro.obtener_movimientos_por_clave(encodedkey)
        dtos = []
        for entity in entities:
            dtos.append(self._obtener_movimiento_dto(entity))

        return dtos

    def hacer_deposito(self, encodedkey: str, deposito: MovimientoDtoIn) -> IdDto:
        """
        Hace un deposito a un ahorro específico.

        Args:
            encodedkey (str): Clave del ahorro.
            deposito (MovimientoDto): Datos del deposito.

        Returns:
            IdDto: DTO con el id del movimiento realizado.
        """
        if deposito.referencia is None:
            deposito.referencia = uuid4()
        entity = MovimientoEntity(
            cantidad=deposito.cantidad,
            concepto=deposito.concepto,
            referencia=deposito.referencia,
            fecha=datetime.now().isoformat(),
            id=0,
            saldo_final=0.0,
            saldo_inicial=0.0,
            tipo="Deposito",
        )
        self.repo.ahorro.hacer_deposito(encodedkey, entity)

        return IdDto(id=0, encodedkey=deposito.referencia, fecha=str(datetime.now()))

    def hacer_retiro(self, encodedkey: str, retiro: MovimientoDtoIn) -> IdDto:
        """
        Hace un retiro de un ahorro específico.

        Args:
            encodedkey (str): Clave del ahorro.
            retiro (MovimientoDto): Datos del retiro.

        Returns:
            IdDto: DTO con el id del movimiento realizado.
        """
        if retiro.referencia is None:
            retiro.referencia = uuid4()
        entity = MovimientoEntity(
            cantidad=retiro.cantidad,
            concepto=retiro.concepto,
            referencia=retiro.referencia,
            fecha=datetime.now().isoformat(),
            id=0,
            saldo_final=0.0,
            saldo_inicial=0.0,
            tipo="Retiro",
        )
        movimiento = self.repo.ahorro.hacer_retiro(encodedkey, entity)

        return IdDto(id=movimiento.id, encodedkey=movimiento.referencia, fecha=str(datetime.now()))

    def obtener_movimiento_por_clave(self, encodedkey: str) -> MovimientoDto:
        """
        Obtiene un movimiento específico por su clave.

        Args:
            encodedkey (str): Clave del movimiento.

        Returns:
            MovimientoDto: DTO del movimiento.
        """
        entity = self.repo.ahorro.obtener_movimiento_por_clave(encodedkey)
        if entity is None:
            return None

        return self._obtener_movimiento_dto(entity)
    
    # Metodos privados
    def _obtener_dto(self, item: AhorroEntity) -> AhorroDto:
        return AhorroDto(
            id=item.id,
            encodedkey=item.encodedkey,
            fecha=str(item.fecha),
            total=float(str(item.total)),
            nombre=item.nombre,
            clienteGuid=item.cliente_encodedkey,
            estado=item.estado,
            otros=item.otros,
        )

    def _obtener_movimiento_dto(self, item: MovimientoEntity) -> MovimientoDto:
        return MovimientoDto(
            id=item.id,
            cantidad=float(str(item.cantidad)),
            concepto=item.concepto,
            referencia=item.referencia,
            tipo=item.tipo,
            fecha=str(item.fecha),
            saldoInicial=float(str(item.saldo_inicial)),
            saldoFinal=float(str(item.saldo_final)),
        )
