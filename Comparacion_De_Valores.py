import pandas as pd
import matplotlib.pyplot as plt

#carga del documento
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_movies = pd.read_csv(file_path)


#calcular y mostrar el promedio de tomatometer_rating
promedio_criticos = df_movies['tomatometer_rating'].mean()
print(f"Promedio de valoracion por criticos: {promedio_criticos:.2f}")

#calcular y mostrar el promedio de audience_rating.
promedio_audiencia = df_movies['tomatometer_rating'].mean()
print(f"Promedio de valoracion por audiencia: {promedio_audiencia:.2f}")

#Crear una nueva columna llamada rating_diff
df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

#Mostrar las primeras filas con la nueva columna
print(df_movies[['audience_rating', 'tomatometer_rating', 'rating_diff']].head())

#Generar histograma
plt.figure(figsize=[10,6])
df_movies['rating_diff'].plot(kind='hist', bins=30, color='green', edgecolor='black', alpha=0.7)
plt.title('Histograma de diferencias de valoracion "Audiencia y Criticos"')
plt.xlabel('Diferencia en valoracion(rating_diff')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()














