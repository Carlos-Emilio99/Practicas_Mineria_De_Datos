#7.- Forecasting

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats


df = pd.read_csv("C:\\Users\\carlo\\Desktop\\Mineria\\Practicas_Mineria_De_Datos\\Practica1\\nba_game_stats.csv")


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])
print(df_LIMP)

def get_prediction_interval(prediction, y_test, test_predictions, pi=.95):
    sum_errs = np.sum((y_test - test_predictions)**2)
    stdev = np.sqrt(1 / (len(y_test) - 2) * sum_errs)
    one_minus_pi = 1 - pi
    ppf_lookup = 1 - (one_minus_pi / 2)
    z_score = stats.norm.ppf(ppf_lookup)
    interval = z_score * stdev
    lower, upper = prediction - interval, prediction + interval
    return lower, prediction, upper


df_lr = pd.DataFrame({'TeamPoints': df_LIMP['TeamPoints'], 'OpponentPoints': df_LIMP['OpponentPoints']})
X = df_lr['TeamPoints'].values.reshape(-1,1)
Y= df_lr['OpponentPoints']

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

lower_vet = []
upper_vet = []

for i in Y_pred:
    lower, prediction, upper =  get_prediction_interval(i, df_lr['OpponentPoints'], Y_pred)
    lower_vet.append(lower)
    upper_vet.append(upper)

plt.fill_between(np.arange(0,len(df_lr['OpponentPoints']),1),upper_vet, lower_vet, color='b',label='IC = 0.95')
plt.plot(np.arange(0,len(df_lr['OpponentPoints']),1),df_lr['OpponentPoints'],color='orange',label='Datos')
plt.plot(Y_pred,'k',label='Regresión', color = 'red')
plt.xlabel('PuntuacionT')
plt.ylabel('PuntuacionO')
plt.title('Puntuacion')
plt.show()
plt.close()

