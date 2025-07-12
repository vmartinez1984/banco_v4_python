# Banco

## todo
- [ ] Obtener todos los clientes
- [ ] Paginado de clientes
- [ ] Buscar clientes
- [ ] Ahorros

## Clientes

Crud de clientes

Cliente
- Nombre
- Apellido materno
- Apellido parteno
- Fecha de nacimiento
- Curp
- Sexo
- Direccion
    - Calle y número
    - Colonia
    - Codigo postal
    - Alcaldia
    - Estado
    - Referencias
    - coordenadas
- otros
    - llave, valor
- encodedKey
- Número de cliente
- correo
- contraseña

## Depositos

Deposito
- Nombre
- Encodedkey
- Número de deposito
- Balance
- Movimientos
    - Fecha
    - Cantidad inicial
    - Cantidad final
    - Cantidad
    - Tipo de movimiento
    - CanalEncodedKey
    - coordenadas
Canal
- encodedKey
- id
- nombre
- descripción

## Usuarios

Usuario
- Nombre
- Apellido materno
- Apellido parteno
- Fecha de nacimiento
- Curp
- Sexo
- correo
- contraseña

## Run app
En ubuntu
usar un entorno virtual (opcional, pero buena práctica)

    Instala el módulo de entornos virtuales:
```
sudo apt install python3-venv
```

Crea el entorno virtual:
```
python3 -m venv venv
```

Activa el entorno virtual:
```
source venv/bin/activate
```

Instala con pip dentro del entorno:
```
pip install -r requirements.txt
```


```
uvicorn main:app --reload
```
