class PaginadoDto:    
    total: int
    total_filtrados:int
    lista: any

    def __init__(self,         
        total: int,
        total_filtrados:int,
        lista: any):
        """
        docstring
        """
        self.total = total
        self.total_filtrados = total_filtrados
        self.lista = lista
    