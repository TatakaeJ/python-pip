# Version la cual se quiere teneren el contenedor
FROM python:3.12

# Directorio en donde se va a guardar el proyecto
WORKDIR /app
# Librerias y dependencias del proyecto
COPY requirements.txt /app/requirements.txt

# Corre el comando para instalar las librerias y dependencias de requirements
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Agrega todo el proyecto al directorio creado en el contenedor
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]