# Descripción servicio

Este es un proyecto personal. Sirve para buscar canciones y retornar un streaming del audio que deseas usando yt-dpl.

## Requirements
```sh
    $ python --version v3.10.12
```

## Levantar servicio
### 1 crear entorno virtual e instalar dependencias
```sh
    $ python -m venv .venv && source .venv/bin/activate
    $ pip install -r requirements.txt
```

### Correr servicio
```sh
    $ uvicorn app.main:app --host 0.0.0.0 --port 8030 --reload # Si el puerto 8000 esta ocupado utilizar otro
```

## Levantar servicio en docker

### Crear contenedor

Nos paramos en el directorio raíz donde esta nuestro dockerfile y ejecutamos el siguiente comando:
```sh
    $ docker build -t proyectopython .
```

### Levantar contenedor
```sh
    $ docker run --name contepython -dp 8030:8030 proyectopython
```


## Endpoint de prueba  

http://0.0.0.0:8030/api/persofy/v1/health


## Endpoint Swagger

http://0.0.0.0:8030/api/persofy/v1/docs
