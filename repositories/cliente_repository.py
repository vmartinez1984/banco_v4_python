from typing import List
from pymongo import MongoClient
from entities.cliente_entity import ClienteEntity
from entities.contacto_entity import ContactoEntity
from entities.pagiando_entity import PaginadoEntity
from repositories.config import db_name, uri


class ClienteRepository:
    def __init__(self):
        self.cliente = MongoClient(uri)
        self.db = self.cliente[db_name]
        self.collection = self.db["Clientes"]

    def obtener_todos(
        self, paginado: PaginadoEntity
    ) -> PaginadoEntity:
        
        # Pipeline de agregación
        pipeline= None
        if paginado.filtro == "":
            pipeline = [                              
                {"$skip": paginado.obtener_salto()},
                {"$limit": paginado.registros_por_pagina}
            ]
        else:
            pipeline = [
                {
                    "$addFields": {
                        "nombre_completo": {
                            "$concat": ["$Nombre", " ", "$PrimerApellido",]
                        }
                    }
                },
                {
                    "$match": {
                        "nombre_completo": {
                            "$regex": paginado.filtro,
                            "$options": "i"  # Ignora mayúsculas/minúsculas
                        }
                    }
                },
                {"$skip": paginado.obtener_salto()},
                {"$limit": paginado.registros_por_pagina}
            ]
        # print(pipeline)
        inventory = self.collection.aggregate(pipeline)
        inventory = self._obtener_entities(inventory)
        pipeline_total = pipeline[:-2] + [{"$count": "total"}]
        conteo = list(self.collection.aggregate(pipeline_total))
        paginado.total_filtrados = conteo[0]["total"] if conteo else 0        
        paginado.total = self.collection.count_documents({})        
        paginado.lista = inventory
        #print(paginado.total)
        #print(paginado.total_filtrados)

        return paginado

    def obtener_por_clave(self, encodedkey: str) -> ClienteEntity:
        if encodedkey.isdigit():
            item = self.collection.find_one({"Id": int(encodedkey)})
        else:   
            item = self.collection.find_one({"EncodedKey": encodedkey})
        if item is None:
            return None

        return self._obtener_entity(item)
    
# Metodos privados
    def _obtener_entities(self, inventory) -> List[ClienteEntity]:
        entities = []
        for item in inventory:
            entities.append(self._obtener_entity(item))

        return entities

    def _obtener_entity(self, item) -> ClienteEntity:
        # print(item)
        direccion = None
        # if item["Direccion"] !=None:
        #     direccion = DireccionEntity(
        #         calle_numero= item["Direccion"]["calle_numero"]
        #     )
        contactos = []
        if item["Contactos"] != None:
            for contacto in item["Contactos"]:
                contactos.append(
                    ContactoEntity(                        
                        nombre=contacto["Nombre"],
                        alias=contacto["Alias"],
                        cuenta=contacto["Cuenta"],
                        encodedkey=contacto["EncodedKey"],
                        fecha_de_registro=contacto["FechaDeRegistro"],
                        esta_activo=contacto["EstaActivo"],
                    )
                )
        return ClienteEntity(
            id=item["Id"],
            encodedkey=item["EncodedKey"],
            nombre=item["Nombre"],
            primer_apellido=item["PrimerApellido"],
            segundo_apellido=item["SegundoApellido"],
            correo=item["Correo"],
            otros=item["Otros"],
            telefono=item["Telefono"],
            contactos=contactos,
            direccion=direccion,
            esta_activo=item["EstaActivo"],
            fecha_de_nacimiento=item["FechaDeNacimiento"],
            fecha_de_registro=item["FechaDeRegistro"],
        )
