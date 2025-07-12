from business_layer.ahorro_bl import AhorroBl
from business_layer.cliente_bl import ClienteBl


class UnitOfWok:
    def __init__(self):
        self.cliente = ClienteBl()
        self.ahorro = AhorroBl()