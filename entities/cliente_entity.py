from datetime import datetime
from typing import List
from entities.contacto_entity import ContactoEntity
from entities.direccion_entity import DireccionEntity


class ClienteEntity:
    id: int
    encodedkey: str
    primer_apellido: str
    segundo_apellido: str
    correo: str
    nombre: str
    telefono: str
    direccion: DireccionEntity
    esta_activo: bool
    fecha_de_nacimiento: datetime
    fecha_de_registro: datetime
    contactos: List[ContactoEntity]
    otros: dict

    def __init__(
        self,
        id: int,
        encodedkey: str,
        primer_apellido: str,
        segundo_apellido: str,
        correo: str,
        nombre: str,
        telefono: str,
        direccion: DireccionEntity,
        esta_activo: bool,
        fecha_de_nacimiento: datetime,
        fecha_de_registro: datetime,
        contactos: List[ContactoEntity],
        otros: dict
        ):
        self.id = id
        self.encodedkey = encodedkey
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.fecha_de_registro = fecha_de_registro
        self.contactos = contactos
        self.esta_activo = esta_activo
        self.otros = otros