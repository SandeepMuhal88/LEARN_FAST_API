# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# @app.get("/about")
# def about():
#     return {"message": "This is a basic FastAPI application"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/items/")
# def create_item(name: str, price: float):
#     return {"name": name, "price": price}

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}



    