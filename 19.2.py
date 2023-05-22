class Pelicula:
    def __init__(self, titulo, estudio, anio_estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.anio_estreno = anio_estreno


def mostrar_peliculas_anio(peliculas, anio):
    peliculas_anio = [pelicula.titulo for pelicula in peliculas if pelicula.anio_estreno == anio]
    return peliculas_anio


def contar_peliculas_anio(peliculas, anio):
    contador = sum(1 for pelicula in peliculas if pelicula.anio_estreno == anio)
    return contador


def mostrar_peliculas_marvel_anio(peliculas, anio):
    peliculas_marvel_anio = [pelicula.titulo for pelicula in peliculas if pelicula.estudio == "Marvel Studios" and pelicula.anio_estreno == anio]
    return peliculas_marvel_anio

peliculas = [
    Pelicula("Avengers: Age of Ultron", "Marvel Studios", 2015),
    Pelicula("Guardians of the Galaxy", "Marvel Studios", 2014),
    Pelicula("Black Panther", "Marvel Studios", 2018),
    Pelicula("Doctor Strange", "Marvel Studios", 2016),
    Pelicula("Iron Man 3", "Marvel Studios", 2013)
]

peliculas_2014 = mostrar_peliculas_anio(peliculas, 2014)
print("Películas estrenadas en 2014:")
for pelicula in peliculas_2014:
    print(pelicula)

cantidad_peliculas_2018 = contar_peliculas_anio(peliculas, 2018)
print("Cantidad de películas estrenadas en 2018:", cantidad_peliculas_2018)

peliculas_marvel_2016 = mostrar_peliculas_marvel_anio(peliculas, 2016)
print("Películas de Marvel Studios estrenadas en 2016:")
for pelicula in peliculas_marvel_2016:
    print(pelicula)





