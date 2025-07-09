import re
from pydantic import BaseModel


class AhorroDto(BaseModel):
    id: int
    encodedkey: str
    fecha: str
    total: float
    nombre: str
    clienteEncodedKey: str
    estado: str
    otros: dict

    def to_dict(self):
        return {
            "id": self.id,
            "encodedkey": self.encodedkey,
            "fecha": self.fecha,
            "total": self.total,
            "nombre": self.nombre,
            "clienteEncodedKey": self.clienteEncodedKey,
            "estado": self.estado,
            **self.otros
        }