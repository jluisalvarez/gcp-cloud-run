# Docker, python y Flask (Hola Mundo)


## Crea la aplicación

Crea un entorno virtual, actívalo e instala Flask.
(aquí no crearemos el entorno vírtual, pero es muy aconsejable hacerlo)

```shell
$ pip3 install flask
```

Implementa la aplicación, por ejemplo en el fichero app.py:

```python
# file app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola Mundo!'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)


```

Prueba la aplicación en local


```shell
$ python3 app.py
```



## Contruir la imagen

Crea el fichero Dockerfile

```
FROM python:3.6

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

```

Construye la imagem

```shell
$ docker build --tag jluisalvarez/hm-python:2023 .
```

Prueba la imagen en local

```shell
$ docker run -d --name hmpython -p 8080:8080 jluisalvarez/hm-python:2023
```

Sube la imagen a Docker Hub

```shell
$ docker login

...

$ docker push jluisalvarez/hm-python:2023

```

# Despliega en GCP Cloud Run

En la consola web de GCP, selecciona Cloud Run en la sección Serveless.


Selecciona crear servicio "Create Service"

En "Container image URL" introduce la imagen, por ejemplo, jluisalvarez/hm-python:2023.

En "Name Service" introduce el nombre, por ejemplo, hm-python y selecciona la región, por ejemplo, europe-southwest1 (Madrid).

En Autoscaling, introduce en Minimum number of instances: 0 y en Maximum number of instances: 10; y selecciona All (Allow direct access to your service from the interne).

En Authentication, marca la opción Allow unauthenticated invocations (Check this if you are creating a public API or website)

Revisa los valores de las secciones Container, Networking, Security; 
asegúrate que en Container el puerto coincide con el que expone la aplicación, selecciona la CPU y Memoria deseada y el entorno por defecto.

El resto de las opciones puedes dejarlas por defecto y pulsar en Crear.

Cuando se complete la acción, podrá acceder al contenedor con la URL del tipo https://hm-python-xxxxxxxxxx-no.a.run.app/








