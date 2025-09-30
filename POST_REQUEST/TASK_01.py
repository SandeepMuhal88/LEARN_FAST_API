from pydantic import BaseModel,Field, computed_field,field_validator
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from typing import Annotated, Literal,Optional


app=FastAPI()

# Load data (with error handling)
def load_data():
    try:
        with open('user.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}  
    return data

#Save data
def save_data(data):
    with open('user.json','w') as f:
        json.dump(data,f)


# Make A pydantic model for Data Vlidatation 

class Patient(BaseModel):

    id:Annotated[str,Field(..., description='ID of the patient',examples=['22EBUCS001'])]
    name:Annotated[str,Field(...,description="Name of the patient")]
    city:Annotated[str,Field(...,description="City of the Patients where is is living",examples=['Ajmer'])]
    age: Annotated[int,Field(...,gt=0,lt=120,description="Enter the age of the Patient")]
    gender:Annotated[Literal['Male','Female','Other'],Field(...,description="Enter the Gender of the Patients")]
    height:Annotated[float,Field(...,gt=0,description="Enter the in Meter")]
    weight:Annotated[float,Field(...,gt=0,description='Enter the Weight of the patients in Kg')]

    # For BMI and Verdict

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->float:
        if self.bmi<18.5:
            return 'Under-Weight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi<30:
            return 'Over-weight'
        else:
            return 'Obese'
        
@app.get('/')
def print_data():
    return {"Message":"Welcome to the Patient Management System"}


@app.post('/create')
def create_patients(patient:Patient):
    #load Exiting data
    data=load_data()
    #check the patients already exits in database
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patients already exits')
    #Add new patients in database
    # Pydantic obj ko dictionay ke andar convert 
    data[patient.id]=patient.model_dump(exclude=['id'])
    # Save the file
    save_data(data)
    # Return the response
    return JSONResponse(status_code=201,content={'Message':'Patients create succesfully!'})
