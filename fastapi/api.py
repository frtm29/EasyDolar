import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from EasyDolar.archivo_python_modelo_predicción import load_model #actualizar con archivo modelo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.state.model = load_model() #debemos cargar el modelo entrenado como load_model()para despues dejarlo resitrado en la app

@app.get('/predict')
def predict(email: str, date: str):
    X_pred = pd.DataFrame(locals(), index=[0])
    model = app.state.model #Podria faltar prepropesar los datos, haciendo alguna funcion que indique de que forma es factible pasar los datos, es decir, si se pasan en otro formato que indique error
    y_pred = model.predict(X_pred)
    return dict(USD_CLP=float(y_pred))
