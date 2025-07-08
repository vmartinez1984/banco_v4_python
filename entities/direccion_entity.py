class DireccionEntity:
    calle_numero: str
    referencia: str
    colonia: str
    municipio: str
    codigo_postal: str
    estado: str
    coordenadas_gps: str

    def __init__(
        self,
        municipio: str,
        calle_numero: str,
        codigo_postal: str,
        colonia: str,
        coordenadas_gps: str,
        estado: str,
        referencia: str,
    ):
        self.calle_numero = calle_numero
        self.referencia = referencia
        self.colonia = colonia
        self.municipio = municipio
        self.estado = estado
        self.codigo_postal = codigo_postal
        self.coordenadas_gps = coordenadas_gps
