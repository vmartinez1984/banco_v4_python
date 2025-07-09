from datetime import datetime


class AhorroEntity:
    def __init__(self, 
        id: int, 
        encodedkey: str, 
        total: float,
        nombre: str,        
        cliente_encodedkey: str,
        fecha: datetime, 
        estado:str,
        otros: dict
        ):
        self.id = id
        self.encodedkey = encodedkey
        self.total  = total
        self.nombre = nombre
        self.cliente_encodedkey = cliente_encodedkey
        self.estado = estado
        self.fecha = fecha
        self.otros = otros