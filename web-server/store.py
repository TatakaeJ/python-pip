# requests - libreria que ayuda a optener inforpacion de APIs web
import requests


def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)

    categories = r.json()
    for category in categories:
        print(category["name"])
