from typing import List
from pydantic import BaseModel

from dtos.DireccionDto import ContactoDto, DireccionDto


class ClienteDtoIn(BaseModel):
    encodedKey: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    curp: str
    numero_de_cliente: str
    correo: str
    constrasenia: str
    direccion: DireccionDto


class ClienteDto(BaseModel):
    encodedkey: str
    nombre: str
    primerApellido: str
    segundoApellido: str
    curp: str
    numeroDecliente: str
    correo: str
    telefono: str
    fechaDeNacimiento: str
    fechaDeRegistro: str
    # direccion: DireccionDto
    contactos: List

    def to_dict(self) -> dict:
        return {
            "encodedKey": self.encodedkey,
            "nombre": self.nombre,
            "primerApellido": self.primerApellido,
            "segundoApellido": self.segundoApellido,
            "curp": self.curp,
            "numeroDeCliente": self.numeroDecliente,
            "correo": self.correo,
            "telefono": self.telefono,
            # "direccion": None,  # self.direccion.to_dict()
            "fechaDeNacimiento": self.fechaDeNacimiento,
            "fechaDeRegistro": self.fechaDeRegistro,
            "contactos": self.obtener_contactos_dict(self.contactos),
        }

    def obtener_contactos_dict(self,contactos: List[ContactoDto]) -> List:
        lista = []
        for contacto in contactos:
            print(contacto)
            lista.append(contacto.to_dict())

        return lista
