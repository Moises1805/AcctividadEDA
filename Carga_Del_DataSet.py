import pandas as pd
import matplotlib.pyplot as plt


#lectura del archivo 'Rotten tomatoes movies'
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_movies = pd.read_csv(file_path)

#llamada al dataframe Movies
print(df_movies)

#mostrar las primeros 5 filas del DataFrame.
print(df_movies.head())

#Verificar los tipos de datos de cada columna.
print(df_movies.info())

#convertir la columna 'in_theaters_date' al tipo datetime
#MAnejar errores con errors='coerse' para fechas invalidas

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

#verificar los tipos de datos nuevamente
print(df_movies.dtypes)


# 7. Mostrar si hubo valores no convertidos (NaT)
missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")








