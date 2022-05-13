import pandas as pd

df = pd.read_csv("C:\\Users\\carlo\\Desktop\\Mineria\\Practicas_Mineria_De_Datos\\Practica1\\nba_game_stats.csv")
print(df)

df_LIMP = df.drop(columns = ['FieldGoals.','X3PointShots.','FreeThrows.','Opp.FieldGoals.','Opp.3PointShots.','Opp.FreeThrows.'])
print(df_LIMP)







