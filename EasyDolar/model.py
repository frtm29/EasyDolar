import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

def realizar_prediccion_sarima(data, start, end, order=(1, 1, 1), seasonal_order=(1, 1, 1, 14), lags=6):
    # Dividir los datos en prueba
    test_data = data[(data.index >= start) & (data.index <= end)]

    # Listas para almacenar predicciones y valores reales
    predictions = []
    ground_truth = []

    # Walk Forward Validation
    for test_index in test_data.index:
        # Actualizar el conjunto de entrenamiento con los datos hasta la fecha actual
        current_train_data = data[test_index - pd.DateOffset(days=lags):test_index - pd.DateOffset(days=1)]
        # Ajustar el modelo SARIMA
        model = SARIMAX(current_train_data["close"], order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
        # Realizar la predicción para el siguiente día
        prediction = model_fit.forecast().values[0]
        predictions.append(prediction)
        ground_truth.append(test_data.loc[test_index, "close"])

    return predictions, ground_truth


def evaluar_y_graficar_predicciones(test_data, ground_truth, predictions):
    # Calcular el error medio absoluto
    mae = mean_absolute_error(ground_truth, predictions)
    print("MAE: ", mae)

    # Gráfico de predicciones vs valores reales
    plt.figure(figsize=(10, 6))
    plt.plot(test_data.index, ground_truth, label="Real")
    plt.plot(test_data.index, predictions, label="Predicciones", color="red")
    plt.title("Predicciones SARIMA vs Valores Reales")
    plt.xlabel("Fecha")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()
