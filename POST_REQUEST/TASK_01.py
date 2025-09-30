# from pydantic import BaseModel,Field, computed_field,field_validator
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse
# import json
# from typing import Annotated, Literal,Optional


# app=FastAPI()

# # Load data (with error handling)
# def load_data():
#     try:
#         with open('patients.json', 'r') as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         data = {}  

# #Save data
# def save_data(data):
#     with open('patients.json','w') as f:
#         json.dump(data,f)


# # Make A pydantic model for Data Vlidatation 

# class Patient(BaseModel):

#     id:Annotated[str,Field(..., description='ID of the patient',examples=['P001'])]
#     name:Annotated[str,Field(...,description="Name of the patient")]
#     city:Annotated[str,Field(...,description="City of the Patients where is is living",examples=['Ajmer'])]
#     age:Annotated(int,Field(...,gt=0,lt=120,description="Enter the age of the Patient"))
#     gender:Annotated[Literal['Male','Female','Other'],Field(...,description="Enter the Gender of the Patients")]
#     height:Annotated[float,Field(...,gt=0,description="Enter the in Meter")]
#     weight:Annotated[float,Field(...,gt=0,description='Enter the Weight of the patients in Kg')]

#     # For BMI and Verdict

#     @computed_field
#     @property
#     def bmi(self)->float:
#         bmi=round(self.weight/(self.height**2),2)
#         return bmi
    
#     @computed_field
#     @property
#     def verdict(self)->float:
#         if self.bmi<18.5:
#             return 'Under-Weight'
#         elif self.bmi<25:
#             return 'Normal'
#         elif self.bmi<30:
#             return 'Normal'
#         else:
#             return 'Over-weight'
        

# @app.post('/create')
# def create_patients(patient:Patient):
#     #load Exiting data
#     data=load_data()
#     #check the patients already exits in database
#     if patient.id in data:
#         raise HTTPException(status_code=400,detail='Patients already exits')
#     #Add new patients in database
#     # Pydantic obj ko dictionay ke andar convert 
#     data[patient.id]=patient.model_dump(exclude=['id'])
#     # Save the file
#     save_data(data)
#     # Return the response
#     return JSONResponse(status_code=201,content={'Message':'Patients create succesfully!'})
from pydantic import BaseModel, Field, computed_field
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from typing import Annotated, Literal

app = FastAPI()

# Load data (with error handling)
def load_data():
    try:
        with open('patients.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}  # Return an empty dict if the file doesn't exist
    return data

# Save data
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4) # Added indent for readability

# Pydantic model for Data Validation
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City of the Patients where is is living", examples=['Ajmer'])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Enter the age of the Patient")]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description="Enter the Gender of the Patients")]
    height: Annotated[float, Field(..., gt=0, description="Enter the height in Meter")]
    weight: Annotated[float, Field(..., gt=0, description='Enter the Weight of the patients in Kg')]

    @computed_field
    @property
    def bmi(self) -> float:
        """Calculates Body Mass Index (BMI)."""
        return round(self.weight / (self.height ** 2), 2)
    
    # ✅ FIXED: Return type is now 'str' and logic is corrected
    @computed_field
    @property
    def verdict(self) -> str:
        """Determines the weight category based on BMI."""
        if self.bmi < 18.5:
            return 'Under-Weight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Over-weight'
        else:
            return 'Obese'

@app.post('/create')
def create_patient(patient: Patient):
    """Creates a new patient record."""
    # Load existing data
    data = load_data()
    
    # Check if the patient already exists in the database
    if patient.id in data:
        raise HTTPException(status_code=400, detail=f'Patient with ID {patient.id} already exists.')
    
    # Add new patient to the database
    # Pydantic obj ko dictionary ke andar convert
    data[patient.id] = patient.model_dump(exclude={'id'})
    
    # Save the file
    save_data(data)
    
    # Return the response
    return JSONResponse(status_code=201, content={'message': f'Patient {patient.name} created successfully!'})