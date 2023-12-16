import pandas as pd
import matplotlib.pyplot as plt

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    #extraer la data
    data=pd.read_excel("raw_data/data.xlsx")
    #data=pd.read_excel("/Users/juancorreav/code/frtm29/EasyDolar/raw_data/data.xlsx")
    data['variacion'] = data['variacion'].str.rstrip('%').str.replace(',', '.').astype('float') / 100.0
    # Convertir la columna "date" a formato de fecha
    data['date'] = pd.to_datetime(data['date'], format='%d.%m.%Y')

    # Establecer la columna "date" como índice
    data.set_index('date', inplace=True)
    # Ordenar el DataFrame por fechas de forma ascendente
    data.sort_index(inplace=True)
    #Target es nuestro valor a predecir
    data["target"]=data["close"].shift(-1)
    df = pd.DataFrame()
    result = clean_data(df)
    print("✅ data cleaned")
    return result["target"]
