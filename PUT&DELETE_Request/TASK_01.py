from fastapi import FastAPI
from pydantic import Field,BaseModel, computed_field,field_validator
import json
from typing import Annotated,Optional,Literal

app =FastAPI()


# Load the data
def load_data():
    try:
        with open('patients.json','r') as f:
            data=json.load(f)
            return data
    except FileNotFoundError:
        return {'File not Found please add some data first'}
    
# Save Function
def save_data(data):
    try:
        with open('patients.json','w') as f:
            json.dump(data,f,indent=4)
            return {'Data saved successfully'}
    except Exception as e:
        return {'Error':str(e)}

class Patients(BaseModel):
    id:Annotated[str,Field(...,description='ID of the patient',examples='P001')]
    name: Annotated[str,Field(...,description='Name of the Patient')]
    city: Annotated[str,Field(...,description='City of the Patient')]
    age: Annotated[int,Field(...,gt=0,lt=120,description='Age of the Patient')]
    gender: Annotated[Literal['Male','Female','Other'],Field(...,description='Gender of the Patient')]
    height: Annotated[int,Field(...,gt=0,description='Height of the Patient')]
    weight: Annotated[int,Field(...,gt=0,description='Weight of the Patient')]

    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight / (self.height ** 2),2)
    
    @computed_field
    @property
    def verdict(self)->float:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obesity'
        
    
@app.post('/create',tags=['Patients'])
def create_patient(patient:Patients):
    data=load_data()
    data['patients'].append(patient.model_dump())
    save_data(data)
    return {'Data saved successfully'}

