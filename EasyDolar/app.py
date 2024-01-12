import streamlit as st
from datetime import date
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from metrics import directional_accuracy_f, buy_and_hold, suma_de_retornos_diarios

# Cargar el archivo CSV
def load_data(csv_path):
    data = pd.read_csv(csv_path)
    data['date'] = pd.to_datetime(data['date'])
    return data

# Actualización de la función para filtrar datos por fecha
def filter_data_by_date(data, start_date, end_date):
    mask = (data['date'] >= start_date) & (data['date'] <= end_date)
    return data.loc[mask]

def main():
    st.title('Easy Dolar')

    # Carga de datos
    data = load_data('EasyDolar/predicciones.csv')

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Fecha de Inicio', date.today())
    with col2:
        end_date = st.date_input('Fecha Fin', date.today())

    if start_date <= end_date:
        filtered_data = filter_data_by_date(data, pd.to_datetime(start_date), pd.to_datetime(end_date))

        if st.button('Presentar métricas'):

            # Cálculo de métricas
            #accuracy = directional_accuracy_f(filtered_data)
            buy_hold_result = buy_and_hold(filtered_data) * 100
            estrategia_result = suma_de_retornos_diarios(filtered_data) * 100

            # Presentación de métricas
            #st.metric(label='Accuracy', value=f'{accuracy:.2f}')
            st.metric(label='Buy-Hold', value=f'{buy_hold_result:.2f}%')
            st.metric(label='Estrategia', value=f'{estrategia_result:.2f}%')

        # Creación del gráfico
        plt.figure(figsize=(10, 6))
        # Graficar las series con etiquetas y colores
        plt.plot(filtered_data['date'], filtered_data['close'], label='Real', color='red', linewidth=2)
        plt.plot(filtered_data['date'], filtered_data['predictions'], label='Predicción', color='green', linewidth=2)
        # Resaltar el valor de cada serie
        plt.text(filtered_data['date'].iloc[-1], filtered_data['close'].iloc[-1], 'Real', color='white', ha='right')
        plt.text(filtered_data['date'].iloc[-1], filtered_data['predictions'].iloc[-1], 'Predicción', color='white', ha='right')
        # Plotear el gráfico
        plt.title('Predicciones modelo vs Valores Reales', color='white')
        plt.xlabel('Fecha', color='white')
        plt.ylabel('Valor', color='white')
        plt.legend()
        plt.grid(True, axis='y')
        plt.gca().set_facecolor('#000000')  # Establecer el color de fondo del eje
        plt.gcf().set_facecolor('#000000')  # Establecer el color de fondo de la figura
        plt.tick_params(axis='x', colors='white')  # Establecer color de las etiquetas del eje x
        plt.tick_params(axis='y', colors='white')  # Establecer color de las etiquetas del eje y
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        plt.tight_layout()
        # Mostrar el gráfico en Streamlit
        st.pyplot(plt)

    else:
        st.error('La fecha final debe ser posterior a la fecha de inicio.')

if __name__ == '__main__':
    main()
