import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'Fecha demo day': "predicción dolar"}
