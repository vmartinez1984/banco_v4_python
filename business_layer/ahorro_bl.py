from typing import List
from dtos.AhorroDto import AhorroDto
from entities.ahorro_entity import AhorroEntity
from repositories.repository import Respository


class AhorroBl:
    def __init__(self):
        self.repo = Respository()

    def obtener_ahorros_por_cliente(self, encodedkey: str) -> List[AhorroDto]:
        """
        Obtiene todos los ahorros de un cliente específico.
        """
        entities = self.repo.ahorro.obtener_ahorros_por_cliente(encodedkey)
        dtos = [self._obtener_dto(item) for item in entities]

        return dtos


# Metodos privados
    def _obtener_dto(self, item:AhorroEntity) -> AhorroDto:
        return AhorroDto(
            id=item.id,
            encodedkey=item.encodedkey,
            nombre=item.nombre,
            total=item.total,
            cliente_id=item.cliente_id,
            fecha=str(item.fecha) if item.fecha else None,
            estado=item.estado
        )
    