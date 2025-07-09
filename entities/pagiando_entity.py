class PaginadoEntity:
    pagina_actual:int
    registros_por_pagina:int
    filtro: str
    total: int
    total_filtrados:int
    lista: any

    def obtener_salto(self):
        return (self.pagina_actual - 1) * self.registros_por_pagina