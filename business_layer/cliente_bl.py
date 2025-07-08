from typing import List
from dtos.ClienteDto import ClienteDto
from dtos.DireccionDto import ContactoDto
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
    def _obtener_dto(self, item: ClienteEntity) -> ClienteDto:
        direccion = None
        # if self.dir
        contactos = []
        if item.contactos != None:
            for contacto in item.contactos:
                # print(contacto)
                contactos.append(ContactoDto(
                    nombre= contacto.nombre,            
                    cuenta= contacto.cuenta,
                    alias= contacto.alias,
                    fechaDeRegistro= str(contacto.fecha_de_registro),
                    encodedkey= contacto.encodedkey
                ))
            
        return ClienteDto(
            encodedkey=item.encodedkey,
            nombre=item.nombre,
            primerApellido=item.primer_apellido,
            segundoApellido=item.segundo_apellido,
            curp="",
            numeroDecliente=str(item.id),
            correo=item.correo,
            telefono=item.telefono,
            fechaDeRegistro= str(item.fecha_de_registro),
            fechaDeNacimiento=str(item.fecha_de_nacimiento),
            # direccion=direccion
            contactos = contactos
        )

    def _obtener_dtos(self, entities: List[ClienteEntity]) -> List[ClienteDto]:
        dtos = []
        for entity in entities:
            print(entity.contactos)
            dtos.append(self._obtener_dto(entity))

        return dtos
