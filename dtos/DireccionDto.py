from pydantic import BaseModel


class DireccionDto(BaseModel):
    calle_y_numero: str
    colonia:str
    codigo_postal:str
    alcaldia: str
    estado: str
    coordenadas_gps: str