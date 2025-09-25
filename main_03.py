# # that imporve version of main_02.py
# #that have HTTPException


# from fastapi import HTTPException, FastAPI, Path
# import json

# app=FastAPI()

# def load_data():
#     with open("patients.json","r") as f:
#         data=json.load(f)
#     return data


# @app.get("/")
# def about():
#     return {'message':'Patient Management System API'}


# @app.get("/patients")
# def get_patients():
#     return load_data()


# @app.get("/patients/{patient_id}",tags=["Patients"],summary="View a specific patient")
# def view_patient_id(patient_id:str=Path(...,description="Patient ID",example="P001")):
#     data=load_data()
#     if patient_id in data:
#         return data[patient_id]
#     raise HTTPException(status_code=404,detail="Patient not found") 





from fastapi import HTTPException, FastAPI, Path
import json
app=FastAPI()


def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data



@app.get("/")
def about():
    return {'message':'Patient Management System API'}

@app.get("/Home")
def Home():
    return {'We Are working on the A HealthCare Industry'}

@app.get('/patient')
def get_patient():
    data=load_data()
    return data


@app.get("/patient/{patient_id}")
def get_patient_id(patient_id:str):
    dataset=load_data()
    if patient_id in dataset:
        return dataset[patient_id]
    else:
        return {'Id Not Found in database'}


# Update the with Paths

@app.get("/patients/{patient_id}",tags=["Patients"],summary="View a specific patient")
def view_patient_id(patient_id:str=Path(...,description="Patient ID",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found") 