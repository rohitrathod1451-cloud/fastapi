from fastapi import FastAPI ,HTTPException
import json

def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)

    return data    


app = FastAPI()

@app.get("/")
def hello():
    return {'message':"hello world"}   

@app.get("/about")

def about():
    return {'about': 'my name is rohit rajput '}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "patient is not found"}

@app.get("/sort")
def sort_patient(sort_by:str,order:str):
    valid_fields = ["age"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400)
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400)
    
    data = load_data()
    sort_order = True if order=="desc" else False
    sort_data = sorted(data.values(),key= lambda x: x.get(sort_by,0),reverse = sort_order)

    return sort_data
