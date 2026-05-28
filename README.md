# Game Project

Para correr el juego sigue los siguientes pasos en la terminal:

```sh
cd game
python3 main.py
```

# App Project

Para correr el aplicativo de gráficas desde la terminal:

```sh
git clone
cd app
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Por medio de Docker:

```sh
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose ps
sudo docker-compose exec app-csv bash
```

# Web Server

Para correr el servidor web con uvicorn/fastapi:

```sh
git clone
cd web-server
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
```

Por medio de Docker:

```sh
sudo docker-compose build
sudo docker-compose ps
sudo docker-compose up -d
```