from typing import Optional
from pydantic import BaseModel


class AhorroDto(BaseModel):
    id: int
    encodedkey: str
    fecha: str
    total: float
    nombre: str
    clienteGuid: str
    estado: str
    otros: dict

    def to_dict(self):
        return {
            "id": self.id,
            "encodedkey": self.encodedkey,
            "fecha": self.fecha,
            "total": self.total,
            "nombre": self.nombre,
            "clienteGuid": self.clienteGuid,
            "estado": self.estado,
            **self.otros,
        }


class MovimientoDtoIn(BaseModel):
    referencia: Optional[str] = None  # Identificador unico del movimiento
    cantidad: float
    concepto: str


class MovimientoDto(BaseModel):
    id: int
    referencia: str
    fecha: str
    cantidad: float
    tipo: str
    concepto: str
    saldoInicial: float = 0.0
    saldoFinal: float = 0.0

    def to_dict(self):
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "concepto": self.concepto,
            "referencia": self.referencia,
            "tipo": self.tipo,
            "fecha": self.fecha,
            "saldoInicial": self.saldoInicial,
            "saldoFinal": self.saldoFinal,
        }
