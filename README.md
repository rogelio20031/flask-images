# Carga y vista de imágenes en Postgres con FLASK

Este programa es una API Restful con Flask que permite subir y consultar imagenes,
hecha no de la manera tradicional si no que con flask_restful que permite su escalabilidad
y buena organizacion ya que el codigo se divide en clases

## Todas las tecnologías utilizadas
- Python
- Flask
- Flask-RESTful
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose

## Como ejecutar el proyecto
### 1. Clonar el proyecto
```bash
git clone https://github.com/rogelio20031/flask-images.git
```

### 2. Ejecutar con Docker Compose
```bash
docker-compose up --build
```
Esto levantará dos contenedores
-web: la API de Flask corriendo en el puerto 5000
-db: PostgreSQL Corriendo en el puerto 54320

## Como probar la API
### Subida de imagen
- URL: POST /upload
- Body:
- - imag_name: nombre de la imagen (texto)
- - image: archivo (imagen .jpg o .png)

### Obtener imagen por ID
- URL: GET /image/<id>
- Respuesta: La imagen
