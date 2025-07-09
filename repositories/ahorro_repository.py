from pymongo import MongoClient
from entities.ahorro_entity import AhorroEntity
from repositories.config import db_name, uri

class AhorroRepository:
    def __init__(self):
        self.cliente = MongoClient(uri)
        self.db = self.cliente[db_name]
        self.collection = self.db["Ahorros"]

    def obtener_ahorros_por_cliente(self, encodedkey: str) -> list[AhorroEntity]:
        """
        Obtiene todos los ahorros de un cliente específico.
        """
        items = self.collection.find({"ClienteId": encodedkey})
        return [self._obtener_entity(item) for item in items]

#     Metodos privados
    def _obtener_entity(self, item) -> AhorroEntity:
        return AhorroEntity(
            id=item["Id"],
            encodedkey=item["Guid"],
            nombre=item["Nombre"],
            total=item["Total"],
            cliente_id=item["ClienteId"],           
            fecha=item.get("FechaDeRegistro", None),            
            estado=item.get("Estado", "Activo")
        )