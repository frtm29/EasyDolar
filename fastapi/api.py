import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'Fecha demo day': "predicción CLP/USD"}

url = 'http://localhost:8000/predict'

@app.get('/predict')
def predict(email, date):
    model.predict(email, date)
    return {"email":"predicción"}
