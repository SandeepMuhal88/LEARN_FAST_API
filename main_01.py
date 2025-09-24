from fastapi import FastAPI
import json

app=FastAPI()


def load_data():
    with open("patients.json",'r') as f:
        data=json.load(f)
    return data


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}


@app.get("/about")
def about():
    return {'message':'A fully functional API to manage your patients records'}


@app.get("/view")
def get_patients():
    return load_data()

# @app.get("/view/{patient_id}")
# def get_patient(patient_id:str):
#     data=load_data()
#     return data[patient_id]
