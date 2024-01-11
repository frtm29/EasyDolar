import pandas as pd
from fastapi import FastAPI
from model import realizar_prediccion_sarima_completa, evaluar_y_graficar_predicciones

app = FastAPI()


app.state.model = realizar_prediccion_sarima_completa()

@app.get('/predict')
def predict(start_date: str, end_date: str):
    X_pred = pd.DataFrame(locals(), index=[0])
    model = app.state.model #Podria faltar prepropesar los datos, haciendo alguna funciona que indique de que forma es factible pasar os datos, sino indica error
    y_pred = model.predict(X_pred)
    return dict(USD_CLP=float(y_pred))
