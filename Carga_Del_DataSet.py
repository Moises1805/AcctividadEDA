import pandas as pd
import matplotlib.pyplot as plt


file_path = "./Data/Rotten Tomatoes Movies.csv"

#lectura del archivo 'Rotten tomatoes movies'
df_movies = pd.read_csv(file_path)

#llamada al dataframe Movies
print(df_movies)

#mostrar las primeros 5 filas del DataFrame.
print(df_movies.head())

# print(df_movies.info())
# print(df_movies.dtypes())
#
# df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'])
# print(df_movies.dtypes())









