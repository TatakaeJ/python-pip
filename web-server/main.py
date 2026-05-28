from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from store import get_categories

app = FastAPI()


# decorador - donde se establese la ruta
@app.get("/", response_class=HTMLResponse)
async def read_html():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <div>
            <h1>Hola que hace chaval</h1>
            <p>Soy Yusepe el teso</p>
        </div>
    </html>
    """


@app.get("/list")
def get_list():
    return [1, 2, 3, 4]


@app.get("/contact")
def get_contact():
    return {
        "name": "Josepe",
        "phone": "4324522",
    }


def run():
    get_categories()


if __name__ == "__main__":
    run()
