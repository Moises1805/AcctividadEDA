import pandas as pd
import matplotlib.pyplot as plt

#carga del documento
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_movies = pd.read_csv(file_path)

## 1. Contar cuántas películas ha dirigido cada director
conteo_directores = df_movies['directors'].value_counts()

# 2. Mostrar los 10 directores que aparecen con más frecuencia
los_10_directores = conteo_directores.head(10)
print("\nTop 10 directores más frecuentes:")
print(los_10_directores)

# 3. Filtrar el DataFrame para incluir solo las películas de estos 10 directores
los_10_director_names = los_10_directores.index.tolist()
df_top_10 = df_movies[df_movies['directors'].isin(los_10_director_names)].copy()

# 4. Calcular el promedio de tomatometer_rating para las películas de estos directores
promedio_tomatometer = df_top_10.groupby('directors')['tomatometer_rating'].mean()

# Mostrar los promedios de tomatometer_rating
print("\nPromedio de valoración por críticos de los Top 10 directores:")
print(promedio_tomatometer)

# 5. Crear un gráfico de barras simple que muestre los nombres de estos 5 directores y su tomatometer_rating promedio
los_5_directores = promedio_tomatometer.sort_values(ascending=False).head(5)

plt.figure(figsize=(8, 6))
los_5_directores.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Top 5 directores con mejor promedio de valoración por críticos")
plt.xlabel("Calificacion Promedio (Tomatometer) de los Top 5 Directores mas Frecuentes")
plt.ylabel("Director")
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()











