#Funcion que debe recibir los target(dolar a predecir), el dolar del dia anterior y el dolar del día siguiente y el dolar siguiente
#El x es el close de nuestra data, el y_real es el target y el y_pred es la predicción de nuestro modelo
import numpy as np
from sklearn.metrics import make_scorer
def directional_accuracy_f(data):
    direction_real = np.sign(data.close - data.anterior)
    direction_pred = np.sign(data.predictions - data.anterior)
    #valid_directions = direction_real * direction_pred != 0
    return np.mean(direction_real * direction_pred > 0) #& valid_directions
#directional_accuracy=make_scorer(directional_accuracy_f,greater_is_better=True)
#Funcion para predecir los retornos, no hay backtesting tan real
def retornos_f (data):
    direction_real = np.sign(data.close - data.anterior)
    direction_pred = np.sign(data.predictions - data.anterior)
    retorno=np.sum((direction_real*direction_pred)*np.abs(data.close - data.anterior))
    return retorno
def retorno_solo_comprar(data):
    direction_real = np.sign(data.close - data.anterior)
    direction_pred = np.sign(data.predictions - data.anterior)

    retorno = np.sum((direction_real * direction_pred * np.abs(data.close - data.anterior))[direction_pred > 0])
    return retorno
def suma_de_retornos_diarios(data):
    direction_real = np.sign(data.close - data.anterior)
    direction_pred = np.sign(data.predictions - data.anterior)

    retorno = np.sum((direction_real * direction_pred * (np.abs(data.close - data.anterior)/data.anterior))[direction_pred > 0])
    return retorno
#retornos=make_scorer(retornos_f,greater_is_better=True)

def buy_and_hold(data):
    return (data.close.iloc[-1]/data.close.iloc[0])-1
