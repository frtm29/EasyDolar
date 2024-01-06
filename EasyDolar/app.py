import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import requests
import datetime

# Function to simulate data generation for metrics and plot
def generate_data(start_date, end_date):
    # Generate date range
    dates = pd.date_range(start_date, end_date)
    # Simulate some data
    data = np.random.rand(len(dates), 3)
    return dates, data

# Streamlit application
def main():
    st.title('Easy Dolar')

    # Side-by-side date input
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Fecha de Inicio', date.today())
    with col2:
        end_date = st.date_input('Fecha Fin', date.today())

    # Check if end_date is not before start_date
    if start_date <= end_date:
        # Display metrics
        dates, data = generate_data(start_date, end_date)
        st.metric(label='Accuracy', value=f'{data[:,0].mean():.2f}')
        st.metric(label='Buy-Hold', value=f'{data[:,1].mean():.2f}')
        st.metric(label='Estrategia', value=f'{data[:,2].mean():.2f}')

        # Display plot
        fig, ax = plt.subplots()
        ax.plot(dates, data)
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.legend(['Accuracy', 'Buy-Hold', 'Estrategia'])
        st.pyplot(fig)
    else:
        st.error('End date must be after start date.')

# Run the application
if __name__ == '__main__':
    main()
