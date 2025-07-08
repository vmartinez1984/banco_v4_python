from pydantic import BaseModel

from dtos.DireccionDto import DireccionDto

class ClienteDtoIn(BaseModel):
    encodedKey: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    curp:str
    numero_de_cliente:str
    correo:str
    constrasenia:str
    direccion: DireccionDto

class ClienteDto(BaseModel):
    encodedKey: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    curp:str
    numero_de_cliente:str
    correo:str    
    direccion: DireccionDto