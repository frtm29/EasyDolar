import streamlit as st
from datetime import date
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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
        # Generación de datos
        dates = pd.date_range(start='2022-12-01', periods=120, freq='D')
        accuracy = np.random.normal(0.5, 0.1, size=dates.size).cumsum() + 100  # Datos para 'Accuracy'
        buy_hold = np.random.normal(0.3, 0.1, size=dates.size).cumsum() + 100   # Datos para 'Buy-Hold'
        estrategia = np.random.normal(0.4, 0.1, size=dates.size).cumsum() + 100 # Datos para 'Estrategia'

        # Creación del gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(dates, accuracy, label='Accuracy', color='green', linewidth=2)
        ax.plot(dates, buy_hold, label='Buy-Hold', color='red', linewidth=2)
        ax.plot(dates, estrategia, label='Estrategia', color='blue', linewidth=2)

        # Resaltar el último valor de cada serie
        ax.text(dates[-1], accuracy[-1], 'Accuracy', color='green', ha='right')
        ax.text(dates[-1], buy_hold[-1], 'Buy-Hold', color='red', ha='right')
        ax.text(dates[-1], estrategia[-1], 'Estrategia', color='blue', ha='right')

        # Decoración del gráfico
        ax.set_title('Invierte en el Fondo Mutuo BTG Pactual Chile Acción', color='white')
        ax.set_xlabel('Date', color='white')  # Etiqueta del eje x
        ax.set_ylabel('Value', color='white')  # Etiqueta del eje y
        ax.legend()
        ax.grid(True)
        ax.set_facecolor('#003366')  # Color de fondo del eje
        fig.patch.set_facecolor('#003366')  # Color de fondo de la figura
        ax.tick_params(axis='x', colors='white')  # Color de las etiquetas del eje x
        ax.tick_params(axis='y', colors='white')  # Color de las etiquetas del eje y
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)

    else:
        st.error('La fecha final debe ser posterior a la fecha de inicio.')

# Ejecutar aplicación
if __name__ == '__main__':
    main()
