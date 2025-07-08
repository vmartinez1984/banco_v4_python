from datetime import datetime


class ContactoEntity:
    nombre: str
    cuenta: str
    alias: str
    fecha_de_registro: datetime
    encodedkey: str
    id: int
    esta_activo: bool