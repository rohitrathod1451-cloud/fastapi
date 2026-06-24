from pydantic import BaseModel,Field,AnyUrl,EmailStr
from fastapi import FastAPI
from typing import List, Dict ,Annotated,Optional

class Patient(BaseModel):
    name : Annotated[str,Field(max_length=50,title="name of patient",examples=['arun',"rohit"])]
    email: EmailStr
    git : str= Optional[AnyUrl]
    age:int=Field(gt=0,lt=100)
    weight : Annotated[float,Field(gt=0,strict=True)]
    married:bool=Field(default=None)
    contact: Dict[str,str]
    allergies : Optional[List[str]]=None

def patient_detail(patient:Patient):
    return{
        "name": patient.name,
        "age": patient.age,
        "email": patient.email,
        "weight": patient.weight,
        "married": patient.married,
        "allergies": patient.allergies

    }
patient_info =                      {'name':"rohit",         'email':'abc@gmail.com',
                'age':33,
                'weight':55.5,'married':False,'contact':{'number':'1234567890'}}

patient1 =(Patient(**patient_info))
print(patient_detail(patient1))

    