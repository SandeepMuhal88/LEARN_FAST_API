from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,field_validator
from typing import Dict,Optional,Annotated
import json

app=FastAPI()
class Product(BaseModel):

    productId:Annotated[str,Field(...,min_length=5,max_length=10,description="Product ID",examples=["C7L-11M"])]
    productName: Annotated[str,Field(...,min_length=3,max_length=50,description="Product Name",examples=["Smart Fitness Tracker"])]
    category:Annotated[str,Field(...,min_length=3,max_length=50,description="Product Category",examples=["Wearables"])]
    brand:Annotated[str,Field(...,min_length=3,max_length=50,description="Product Brand",examples=["FitCore"])]
    price:Annotated[float,Field(...,gt=0,description="Product Price",examples=[3499.00])]
    inStock:Annotated[bool,Field(...,description="Product Stock Status",examples=[True])]
    tags:Annotated[list,Field(...,min_items=1,description="Product Tags",examples=[["health","fitness","waterproof"]])]


# Load dara function

def load_data():
    try:
        with open('database.json','r') as f:
            data=json.load(f)
    except FileNotFoundError:
        data=[]
    return data

@app.get('/')
def get_product():
    return {"message":"Product List"}

@app.post('/create')
def create_product(product:Product):
    #load the data
    data=load_data()
    #check product id is already exists
    if product.productId in [item['productId'] for item in data]:
        raise HTTPException(status_code=400,detail="Product ID already exists")
    
    data[product.productId]=product.model_dump(exclude=['productId'])
    save_data(data)
    return {"message":"Product created successfully"}