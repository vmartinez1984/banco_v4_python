from pydantic import BaseModel


class DireccionDto(BaseModel):
    calle_numero: str
    colonia:str
    codigoPostal:str
    alcaldia: str
    estado: str
    coordenadasGps: str

    def to_dict(self)-> dict:
        if self == None:
            return None
        return{
            "calle_numero": self.calle_numero,
            "colonia": self.colonia,
            "codigoPostal": self.codigoPostal,
            "alcaldia": self.alcaldia,
            "estado": self.estado,
            "coordenadasGps": self.coordenadasGps
        }
    

class ContactoDto(BaseModel):
    nombre:str
    cuenta:str
    alias:str
    fechaDeRegistro:str
    encodedkey: str

    def to_dict(self)->dict:
        return{
            "nombre": self.nombre,
            "cuenta": self.cuenta,
            "alias": self.alias,
            "fechaDeRegistro": self.fechaDeRegistro,
            "encodedkey:": self.encodedkey
        }