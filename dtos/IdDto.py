from pydantic import BaseModel


class IdDto(BaseModel):
    id: int
    encodedkey: str
    fecha: str


class MensajeDto(BaseModel):
    encodedkey: str
    fecha: str
    mensaje: str

    def to_dict(self):
        return {
            "encodedkey": self.encodedkey,
            "fecha": self.fecha,
            "mensaje": self.mensaje
        }
