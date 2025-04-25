import pandas as pd
import matplotlib.pyplot as plt


#carga del documento
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_movies = pd.read_csv(file_path)


#Cuantas peliculas hay en total.
total_peliculas=len(df_movies)
print(f"El total de peliculas es de: {total_peliculas}")

#Como se distribuyen las calificaciones?
calificaciones= df_movies['tomatometer_status'].value_counts()
print(calificaciones)

#Visualizar distribucion de calificaciones en garfico circular
plt.figure(figsize=(8,6))
calificaciones.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'gold', 'tomato'],  # Colores para las categorías
    labels=calificaciones.index,
    legend=False,
    explode=(0.1, 0, 0)  # Resalta la primera categoría
)

plt.title("Distribución de calificaciones (Tomatometer Status)")
plt.ylabel('')  # Opcional: remover etiqueta del eje Y
plt.show()

