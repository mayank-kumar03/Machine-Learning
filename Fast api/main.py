from fastapi import FastAPI, Path,HTTPException,Query
from pydantic import BaseModel ,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse
import json

class Patient(BaseModel):
     id:Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
     name:Annotated[str,Field(...,description='Name of the patient')]
     city:Annotated[str,Field(...,description='Name of city')]
     age:Annotated[int,Field(...,description='Age of patient',gt=0,lt=120)]
     gender:Annotated[Literal['male','female,Neutral'],Field(...,description='age of patient')]
     height:Annotated[float,Field(...,description='height of the patient',gt=0)]
     weight:Annotated[float,Field(...,description='weight of the patient',gt=0)]
     @computed_field
     @property
     def bmi(self)->float:
          bmi=round(self.weight/(self.height**2),2)
          return bmi
     @computed_field
     @property
     def verdict(self)->str:
          if self.bmi<18.5:
               return 'underweight'
          elif self.bmi<30:
               return 'normal'
          else:
               return 'obese'



app=FastAPI()
def load_data():
      with open('patients.json','r') as f:
         data=json.load(f)   
      return data
def save_data(data):
     with open('patients.json','w') as f:
          json.dump(data,f)

@app.get("/")
def hello():
      return {'message':'Patient History management system api'}

@app.get("/myself")
def myself():
      return {'intro':'A fully functional API to manage your patients record'}


@app.get('/view')
def view():
    data=load_data() 
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='Id of the patient:P001')):
     data=load_data()

     if patient_id in data:
          return data[patient_id]
     raise HTTPException(status_code=404,detail='Patient not found')



@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
@app.post('/create')
def create_patient(patient:Patient):
     #load exiting data
     data=load_data()

     #check existence
     if patient.id in data:
          raise HTTPException(status_code=400,detail='Patient already exists')


     #new patient add to the data
     data[patient.id]=patient.model_dump(exclude=['id'])
     save_data(data)


     return JSONResponse(status_code=201,content={'message':'patient creted successfully'})



      