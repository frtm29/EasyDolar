import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
#Start tiene que ser 2000-03-01
#END tiene que ser el 2023-12-15
def realizar_prediccion_sarima_completa(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 5), lags=41): #alfinal son 40 dias de lags, pero pongo 6 por como esta construido el código,
    test_data = data[42:]
    # Walk Forward Validation
    for test_index in test_data.index:
        # Actualizar el conjunto de entrenamiento con los datos hasta la fecha actual
        current_train_data = data[test_index - pd.DateOffset(days=lags):test_index - pd.DateOffset(days=1)]

        # Ajustar el modelo SARIMA
        model = SARIMAX(current_train_data["close"], order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)

        # Realizar la predicción para el siguiente día
        prediction = model_fit.forecast().values[0]

        # Agregar la predicción al DataFrame original
        test_data.loc[test_index, 'predictions'] = prediction
    condiciones=(test_data['predictions'] > 1500) | (test_data['predictions'] < 300)
    test_data.loc[condiciones, 'predictions'] = test_data['predictions'].mask(condiciones).ffill()
    return test_data


def evaluar_y_graficar_predicciones(test_data): #Este tiene que ser un test_data ya filtrado con las fechas a elegir, no completo
    # Calcular el error medio absoluto
    #mae = mean_absolute_error(ground_truth, predictions)
    #print("MAE: ", mae)

    # Gráfico de predicciones vs valores reales
    plt.figure(figsize=(10, 6))
    plt.plot(test_data.index, test_data.close, label="Real")
    plt.plot(test_data.index, test_data.predictions, label="Predicciones", color="red")
    plt.title("Predicciones SARIMA vs Valores Reales")
    plt.xlabel("Fecha")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()
