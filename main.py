import uvicorn
from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

products: List[Dict[str, Any]] = [
    {
        "id": 1,
        "name": "Smartphone",
        "description": "A telephone that is smart",
        "price": 1500.0,
        "available": True,
    },
    {
        "id": 2,
        "name": "SmartTV",
        "description": "A TV that is smart",
        "price": 2500.0,
        "available": True,
    },
    {
        "id": 3,
        "name": "Smartwatch",
        "description": "A watch that is smart",
        "price": 1000.0,
        "available": False,
    },
]


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/products")
def list_products():
    return products


# if __name__ == "__main__":
uvicorn.run(app, port=8000)
