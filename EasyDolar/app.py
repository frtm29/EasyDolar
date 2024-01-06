import streamlit as st
from datetime import date
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Asumiendo que el servidor FastAPI está corriendo en localhost en el puerto 8000
API_URL = "http://localhost:8000/predict"

# Función para simular los datos para las métricas y el gráfico. Se debe reemplazar por los datos reales
def generate_data(start_date, end_date):
    # Generate date range
    dates = pd.date_range(start_date, end_date)
    # Simulate some data
    data = np.random.rand(len(dates), 3)
    return dates, data

def main():
    st.title('Easy Dolar')

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Fecha de Inicio', date.today())
    with col2:
        end_date = st.date_input('Fecha Fin', date.today())

    # Validar si la fecha de inicio no es mayor que la fecha fin
    if start_date <= end_date:
        if st.button('Presentar métricas'):
            # Aquí es donde haces la solicitud a tu API de FastAPI
            # Asumiendo que tu API necesita un 'email' y una 'date' como parámetros
            response = requests.get(API_URL, params={'email': 'tuemail@example.com', 'date': start_date.isoformat()})
            if response.status_code == 200:
                prediction = response.json()
                st.success(f"Predicción del tipo de cambio USD/CLP: {prediction['USD_CLP']:.2f}")
            else:
                st.error("Hubo un error con la solicitud a la API")

        # Mostrar métricas
        dates, data = generate_data(start_date, end_date)
        st.metric(label='Accuracy', value=f'{data[:,0].mean():.2f}')
        st.metric(label='Buy-Hold', value=f'{data[:,1].mean():.2f}')
        st.metric(label='Estrategia', value=f'{data[:,2].mean():.2f}')

        # Mostrar gráfico
        fig, ax = plt.subplots()
        ax.plot(dates, data)
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.legend(['Accuracy', 'Buy-Hold', 'Estrategia'])
        st.pyplot(fig)
    else:
        st.error('La fecha final debe ser posterior a la fecha de inicio.')

# Ejecutar aplicación
if __name__ == '__main__':
    main()
