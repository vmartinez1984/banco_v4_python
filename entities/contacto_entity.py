from datetime import datetime


class ContactoEntity:
    nombre: str
    cuenta: str
    alias: str
    fecha_de_registro: datetime
    encodedkey: str
    #id: int
    esta_activo: bool

    def __init__(
        self,
        nombre: str,
        cuenta: str,
        alias: str,
        fecha_de_registro: datetime,
        encodedkey: str,
        #id: int,
        esta_activo: bool,
    ):
        self.nombre = nombre
        self.cuenta = cuenta
        self.alias = alias
        self.fecha_de_registro = fecha_de_registro
        self.encodedkey = encodedkey
        #self.id = id
        self.esta_activo = esta_activo
