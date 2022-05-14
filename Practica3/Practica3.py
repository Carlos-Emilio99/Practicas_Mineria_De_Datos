#3.- Analisis de Datos

import pandas as pd

df = pd.read_csv("C:\\Users\\carlo\\Desktop\\Mineria\\Practicas_Mineria_De_Datos\\Practica1\\nba_game_stats.csv")


df_LIMP = pd.DataFrame.from_dict(df.loc[:,['Team','Date','Home','Opponent','WINorLOSS','TeamPoints','OpponentPoints']])
print(df_LIMP)

mean_df = df_LIMP['OpponentPoints'].mean()
print(mean_df)#Se esta mandando el promedio del OpponentPoints

mean_df = df_LIMP['TeamPoints'].mean()
print(mean_df)#Se esta mandando el promedio del TeamPoints

#Se esta imprimiendo la Media, Moda y Mediana de OpponentPoints
media = df["OpponentPoints"].mean()
mediana = df["OpponentPoints"].median()
moda = df["OpponentPoints"].mode()
print("""
    Media OpponentPoints: %d
    Mediana OpponentPoints: %d
    Moda OpponentPoints: %d
""" % (media,mediana,moda))

#Se esta imprimiendo la Media, Moda y Mediana de TeamPoints
media = df["TeamPoints"].mean()
mediana = df["TeamPoints"].median()
moda = df["TeamPoints"].mode()
print("""
    Media TeamPoints: %d
    Mediana TeamPoints: %d
    Moda TeamPoints: %d
""" % (media,mediana,moda))