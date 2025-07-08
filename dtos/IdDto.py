from pydantic import BaseModel


class IdDto(BaseModel):
    id: int
    encodedkey: str
    fecha: str


class MensajeDto(BaseModel):
    encodedkey: str
    fecha: str
    mensaje: str
