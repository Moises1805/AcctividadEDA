import pandas as pd
import matplotlib.pyplot as plt

#carga del documento
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_movies = pd.read_csv(file_path)


#crear una copia del dataframe original para no madificarlo directamente
df_movies_copia= df_movies.copy()

#Dividir la columna 'genre' por "," y expandir cada genero a su propia fila
df_genres_exploted = df_movies_copia.assign(genre=df_movies_copia['genre'].str.split(',')).explode('genre')

#calcular el promedio de audience_rating para cada genero individual
promedio_genero = df_genres_exploted.groupby('genre')['audience_rating'].mean()

#Ordenar los generos por calificacion promedio de audience en orden descendente
los_10_generos = promedio_genero.sort_values(ascending=False).head(10)

#Mostrar los generos y sus promedios
print(los_10_generos)

#Generacion del grafico de pastes con los 10 generos principales.
plt.figure(figsize=(8,6))
los_10_generos.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['Lightblue', 'blue', 'yellow', 'gray', 'pink', 'brown', 'purple', 'red', 'green', 'orange'])
plt.title("Top 10 peliculas con mejor promedio de valoracion")
plt.ylabel('')
plt.show()















