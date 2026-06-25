from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field, computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd

with open ('model.pkl','rb') as f:
    model = pickle.load(f)


app = FastAPI()

class UserIN(BaseModel):
    gender: Annotated[Literal["Male","Female"],Field(...,description="entet the gender")]
    married:Annotated[Literal["Yes","No"],Field(...,)]
    education: Annotated[Literal["Graduate","Not Graduate"],Field(...)]
    self_employed: Annotated[Literal["Yes","No"],Field(...)]
    income:Annotated[float,Field(...,description="salary in k")]
    credit_his:Annotated[float,Field(...,description="score must be 0 to 1")]
    pro_area:Annotated[Literal["Urban","Semiurban","Rural"],Field(...)]


@app.post('/predict')
def predict_a(data:UserIN):
    input_df=pd.DataFrame([{
        'Gender':data.gender,
        'Married':data.married,
        'Education':data.education,
        'Self_Employed':data.self_employed,
        'ApplicantIncome':data.income,
        'Credit_History':data.credit_his,
        'Property_Area':data.pro_area
    }])
    prediction=model.predict(input_df)[0]

    return JSONResponse(status_code=200,content={'Loan Amounr will be':(prediction)*1000})