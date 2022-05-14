#4.- Graficacion.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\carlo\\Desktop\\Mineria\\Practicas_Mineria_De_Datos\\Practica1\\nba_game_stats.csv")


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])
print(df_LIMP)

#Se graficara los puntos del equipo y del oponente
x_values = df['TeamPoints'].unique()
y_values = df['OpponentPoints'].value_counts().tolist()
ax = plt.subplot() 
ax.set_xticks(x_values)   #Eje x
ax.set_xticklabels(x_values)  #Etiquetas del eje x   
plt.ylabel('Puntos') #Nombre del eje x
plt.bar(x_values, y_values)
plt.show()
plt.close('all')

