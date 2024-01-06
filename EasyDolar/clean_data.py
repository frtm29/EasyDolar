
import pandas as pd
import matplotlib.pyplot as plt
import os

def clean_data():
    current_dir = os.getcwd()

    file_path = os.path.join(current_dir, "raw_data", "data.xlsx") #desde /Users/juancorrea/code/frtm29/EasyDolar

    cleaned_data = pd.read_excel(file_path)

    # Limpiar la columna 'variacion'
    cleaned_data['variacion'] = cleaned_data['variacion'].str.rstrip('%').str.replace(',', '.').astype('float') / 100.0

    # Convertir la columna "date" a formato de fecha
    cleaned_data['date'] = pd.to_datetime(cleaned_data['date'], format='%d.%m.%Y')

    # Establecer la columna "date" como índice
    cleaned_data.set_index('date', inplace=True)

    # Ordenar el DataFrame por fechas de forma ascendente
    cleaned_data.sort_index(inplace=True)

    # Crear la columna "target" como el valor de "close" desplazado
    cleaned_data["anterior"] = cleaned_data["close"].shift(1)

    print("✅ data cleaned")

    return cleaned_data


print(clean_data())
