#Funcion que debe recibir los target(dolar a predecir), el dolar del dia anterior y el dolar del día siguiente y el dolar siguiente
#El x es el close de nuestra data, el y_real es el target y el y_pred es la predicción de nuestro modelo
import numpy as np
from sklearn.metrics import make_scorer
def directional_accuracy_f(y_real, y_pred, x):
    direction_real = np.sign(y_real - x)
    direction_pred = np.sign(y_pred - x)
    return np.mean(direction_real * direction_pred > 0)
#directional_accuracy=make_scorer(directional_accuracy_f,greater_is_better=True)
#Funcion para predecir los retornos, no hay backtesting tan real
def retornos_f (y_real,y_pred,x):
    direction_real = np.sign(y_real - x)
    direction_pred = np.sign(y_pred - x)
    retorno=np.sum((direction_real*direction_pred)*np.abs(y_real-x))
    return retorno
retornos=make_scorer(retornos_f,greater_is_better=True)
