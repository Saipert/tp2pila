class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas


def posicion_personajes(lista, personaje1, personaje2):
    posicion = None
    contador = 1

    for personaje in lista:
        if personaje.nombre == personaje1 or personaje.nombre == personaje2:
            posicion = contador
            break

        contador += 1

    return posicion


def personajes_mas_de_cinco_peliculas(lista):
    personajes_mas_cinco = []

    for personaje in lista:
        if personaje.cantidad_peliculas > 5:
            personajes_mas_cinco.append(personaje)

    return personajes_mas_cinco


def peliculas_viuda_negra(lista):
    contador = 0

    for personaje in lista:
        if personaje.nombre == "Viuda Negra":
            contador = personaje.cantidad_peliculas
            break

    return contador


def mostrar_personajes_iniciales(lista, letras):
    personajes_iniciales = []

    for personaje in lista:
        if personaje.nombre[0].upper() in letras:
            personajes_iniciales.append(personaje)

    return personajes_iniciales


personajes = [
    PersonajeMCU("Iron Man", 10),
    PersonajeMCU("Hulk", 6),
    PersonajeMCU("Viuda Negra", 7),
    PersonajeMCU("Capitán América", 9),
    PersonajeMCU("Rocket Raccoon", 4),
    PersonajeMCU("Groot", 5),
    PersonajeMCU("Doctor Strange", 4),
    PersonajeMCU("Thanos", 3)
]

posicion_rocket_groot = posicion_personajes(personajes, "Rocket Raccoon", "Groot")
print("Posición de Rocket Raccoon y Groot:", posicion_rocket_groot)

personajes_mas_cinco = personajes_mas_de_cinco_peliculas(personajes)
print("Personajes que participaron en más de 5 películas:")
for personaje in personajes_mas_cinco:
    print(f"{personaje.nombre}: {personaje.cantidad_peliculas} películas")

peliculas_viuda_negra = peliculas_viuda_negra(personajes)
print("Número de películas de la Viuda Negra:", peliculas_viuda_negra)

personajes_iniciales = mostrar_personajes_iniciales(personajes, "CDG")
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_iniciales:
    print(personaje.nombre)
