from pydantic import BaseModel


class TransaccionDtoIn(BaseModel):
    cantidad: float
    encodedkey: str
    canal: str
    concepto: str
    referencia: str
    coordenadas_gps:str

class TransaccionDto(BaseModel):
    encodedkey: str
    cantidad: float
    cantidad_inicial:float
    cantidad_final:float
    tipo_de_movimiento:str
    canal:str
    coordenadas_gps:str
    