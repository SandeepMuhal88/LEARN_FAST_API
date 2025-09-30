from fastapi import FastAPI
from fastapi import Path
import json

app=FastAPI()


def load_data():
    with open("patients.json",'r') as f:
        data=json.load(f)
    return data



@app.get("/")
def about():
    return {'message':'Patient Management System API'}


@app.get("/patients")
def get_patients():
    return load_data()


# @app.get("/patients/{patient_id}")
# def view_patient_id(patient_id:str):
#     data=load_data()
#     if patient_id in data:
#         return data[patient_id]
#     else:
#         return {'Error':'Patient not found'}


@app.get("/patients/{patient_id}",tags=["Patients"],summary="View a specific patient")
def view_patient_id(patient_id:str=Path(...,description="Patient ID",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {'Error':'Patient not found'}
    
