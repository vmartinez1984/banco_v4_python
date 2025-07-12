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

class MovimientoEntity:
    def __init__(self, 
        id: int, 
        cantidad: float,
        fecha: datetime,
        concepto: str,
        referencia: str,
        saldo_inicial: float,
        saldo_final: float,
        tipo: str
    ):
        self.id = id
        self.cantidad = cantidad
        self.fecha = fecha
        self.concepto = concepto
        self.referencia = referencia
        self.saldo_inicial = saldo_inicial
        self.saldo_final = saldo_final
        self.tipo = tipo

    def to_dict(self):
        return {
            "Id":int(self.id),
            "Cantidad": self.cantidad,
            "FechaDeRegistro": self.fecha.isoformat(),
            "Concepto": self.concepto,
            "Referencia": self.referencia,
            "SaldoInicial": self.saldo_inicial,
            "SaldoFinal": self.saldo_final         
        }