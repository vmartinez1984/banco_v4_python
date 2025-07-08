from typing import List
from pymongo import MongoClient
from entities.cliente_entity import ClienteEntity
from entities.contacto_entity import ContactoEntity
from entities.direccion_entity import DireccionEntity
from repositories.config import db_name, uri


class ClienteRepository:
    def __init__(self):
        self.cliente = MongoClient(uri)
        self.db = self.cliente[db_name]
        self.collection = self.db["Clientes"]

    def obtener_todos(self) -> List[ClienteEntity]:
        inventory = self.collection.find()
        inventory = self._obtener_entities(inventory)
        # print(inventory)
        return inventory

    # Metodos privados
    def _obtener_entities(self, inventory) -> List[ClienteEntity]:
        entities = []
        for item in inventory:            
            entities.append(self._obtener_entity(item))

        return entities

    def _obtener_entity(self, item) -> ClienteEntity:
        #print(item)
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
