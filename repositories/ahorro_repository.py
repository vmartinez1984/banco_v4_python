from datetime import datetime
from typing import List
from pymongo import MongoClient
from entities.ahorro_entity import AhorroEntity, MovimientoEntity
from repositories.config import db_name, uri


class AhorroRepository:
    def __init__(self):
        self.cliente = MongoClient(uri)
        self.db = self.cliente[db_name]
        self.collection = self.db["Ahorros"]

    def obtener_ahorros_por_cliente(self, encodedkey: str) -> List[AhorroEntity]:
        """
        Obtiene todos los ahorros de un cliente específico.
        """
        items = self.collection.find({"ClienteId": encodedkey})
        return [self._obtener_entity(item) for item in items]

    def obtener_movimientos_por_clave(self, encodedkey: str) -> List[MovimientoEntity]:
        """
        Obtiene todos los movimientos de ahorro de un específico.

        Args:
            encodedkey (str): ahorro encoded key o id.

        Returns:
            List[MovimientoEntity]: Lista de movimientos de ahorro.
        """
        if encodedkey.isdigit():
            item = self.collection.find_one({"Id": int(encodedkey)})
        else:
            item = self.collection.find_one({"Guid": encodedkey})
        if item is None:
            return []

        movimientos = item.get("Depositos", [])
        for movimiento in movimientos:
            movimiento["Tipo"] = "Deposito"
        retiros = item.get("Retiros", [])
        for movimiento in retiros:
            movimiento["Tipo"] = "Retiro"
        # Unir los movimientos
        movimientos += retiros
        # Ordenar por fecha
        movimientos = sorted(
            movimientos, key=lambda x: x["FechaDeRegistro"], reverse=True
        )

        return [
            self._obtener_movimiento_entity(movimiento) for movimiento in movimientos
        ]

    def obtener_ahorro_por_clave(self, encodedkey: str) -> AhorroEntity:
        """
        Obtiene un ahorro específico por su clave.

        Args:
            encodedkey (str): Clave del ahorro.

        Returns:
            AhorroEntity: Entidad del ahorro.
        """
        if encodedkey.isdigit():
            item = self.collection.find_one({"Id": int(encodedkey)})
        else:
            item = self.collection.find_one({"Guid": encodedkey})

        if item is None:
            return None

        return self._obtener_entity(item)

    def hacer_deposito(self, encodedkey: str, deposito: MovimientoEntity):
        """
        Hace un deposito a un ahorro específico.

        Args:
            encodedkey (str): Clave del ahorro.
            deposito (MovimientoEntity): Datos del deposito.

        Returns:
            MovimientoEntity: Entidad del movimiento realizado.
        """
        ahorro = None
        if encodedkey.isdigit():
            ahorro = self.collection.find_one({"Id": int(encodedkey)})
        else:
            ahorro = self.collection.find_one({"Guid": encodedkey})
        deposito.fecha = datetime.now()
        deposito.saldo_inicial = float(str(ahorro["Total"]))
        deposito.saldo_final = float(str(ahorro["Total"])) + float(
            str(deposito.cantidad)
        )
        deposito.id = (
            (len(ahorro["Depositos"]) if "Depositos" in ahorro else 0)
            + (len(ahorro["Retiros"]) if "Retiros" in ahorro else 0)
            + 1
        )
        # print(deposito.to_dict())
        ahorro["Total"] = deposito.saldo_final
        ahorro["Depositos"].append(deposito.to_dict())

        item = self.collection.find_one_and_update(
            {"Guid": ahorro["Guid"]}, {"$set": ahorro}
        )
        print(item)

    def hacer_retiro(self, encodedkey: str, retiro: MovimientoEntity):
        """
        Hace un retiro de un ahorro específico.

        Args:
            encodedkey (str): Clave del ahorro.
            retiro (MovimientoEntity): Datos del retiro.

        Returns:
            MovimientoEntity: Entidad del movimiento realizado.
        """
        ahorro = None
        if encodedkey.isdigit():
            ahorro = self.collection.find_one({"Id": int(encodedkey)})
        else:
            ahorro = self.collection.find_one({"Guid": encodedkey})
        if float(str(ahorro.get("Total", 0))) < float(str(retiro.cantidad)):
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        retiro.fecha = datetime.now()
        retiro.saldo_inicial = float(str(ahorro["Total"]))
        retiro.saldo_final = float(str(ahorro["Total"])) - float(str(retiro.cantidad))
        retiro.id = (
            (len(ahorro["Depositos"]) if "Depositos" in ahorro else 0)
            + (len(ahorro["Retiros"]) if "Retiros" in ahorro else 0)
            + 1
        )
        # print(retiro.to_dict())

        ahorro["Total"] = retiro.saldo_final
        ahorro["Depositos"].append(retiro.to_dict())

        item = self.collection.find_one_and_update(
            {"Guid": ahorro["Guid"]}, {"$set": ahorro}
        )
        print(item)

    def obtener_movimiento_por_clave(self, encodedkey: str) -> MovimientoEntity:
        """
        Obtiene un movimiento específico por su clave.

        Args:
            encodedkey (str): Clave del movimiento.

        Returns:
            MovimientoEntity: Entidad del movimiento.
        """
        filtro = {
            "$or": [
                {"Depositos.Referencia": encodedkey},
                {"Retiros.Referencia": encodedkey},
            ]
        }

        item = self.collection.find_one(filtro)
        if item is None:
            return None
        movimientos = item.get("Depositos", [])
        for movimiento in movimientos:
            movimiento["Tipo"] = "Deposito"
        retiros = item.get("Retiros", [])
        for movimiento in retiros:
            movimiento["Tipo"] = "Retiro"
        # Unir los movimientos
        movimientos += retiros
        for movimiento in movimientos:
            if movimiento["Referencia"] == encodedkey:
                return self._obtener_movimiento_entity(movimiento)

    #     Metodos privados
    def _obtener_entity(self, item) -> AhorroEntity:
        return AhorroEntity(
            id=item["Id"],
            encodedkey=item["Guid"],
            nombre=item["Nombre"],
            total=item["Total"],
            cliente_encodedkey=item["ClienteId"],
            fecha=item.get("FechaDeRegistro", None),
            estado=item.get("Estado", "Activo"),
            otros=item.get("Otros", {}),
        )

    def _obtener_movimiento_entity(self, item) -> MovimientoEntity:
        return MovimientoEntity(
            id=item["Id"],
            cantidad=item["Cantidad"],
            fecha=item["FechaDeRegistro"],
            concepto=item["Concepto"],
            referencia=item["Referencia"],
            saldo_inicial=item["SaldoInicial"],
            saldo_final=item["SaldoFinal"],
            tipo=item["Tipo"],
        )
