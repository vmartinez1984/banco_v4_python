from repositories.ahorro_repository import AhorroRepository
from repositories.cliente_repository import ClienteRepository


class Respository:
    def __init__(self):
        self.cliente = ClienteRepository()
        self.ahorro = AhorroRepository()