from typing import List
from dtos.ClienteDto import ClienteDto
from entities.cliente_entity import ClienteEntity
from repositories.repository import Respository


class ClienteBl:
    def __init__(self):
        self.repo = Respository()

    def obtener_todos(self) -> List[ClienteDto]:
        entities = self.repo.cliente.obtener_todos()
        dtos = self._obtener_dtos(entities)

        return dtos

    # privados
    def _obtener_dto(item: ClienteEntity) -> ClienteDto:
        return ClienteDto(
            correo=item.correo,
            curp="",
            direccion="",
            encodedKey=item.encodedkey,
            nombre=item.nombre,
            numero_de_cliente=item.id,
            primer_apellido=item.primer_apellido,
            segundo_apellido=item.segundo_apellido,
        )

    def _obtener_dtos(self, entities: List[ClienteEntity]) -> List[ClienteDto]:
        dtos = []
        for entity in entities:
            dtos.append(self._obtener_dto(entity))

        return dtos
