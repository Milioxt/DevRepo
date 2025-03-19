''' Clases para manejar la base de datos de películas '''
import csv
import os
import hashlib
from datetime import datetime

class Actor:
    ''' Clase para manejar la información de un actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella       = int(id_estrella)
        self.nombre            = nombre
        self.fecha_nacimiento  = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen        = url_imagen
        self.username          = username

    def to_dict(self):
        ''' Devuelve un diccionario con la información del actor '''
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen,
            'username': self.username
        }  

class Pelicula:
    ''' Clase para manejar la información de una película '''
    def __init__(self, id_pelicula, titulo_pelicula, fecha_lanzamiento, url_poster):
        self.id_pelicula    = int(id_pelicula)
        self.titulo_pelicula         = titulo_pelicula
        self.fecha_lanzamiento  = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d').date()
        self.url_poster        = url_poster
    def to_dict(self):
        ''' Devuelve un diccionario con la información de la película '''
        return {
            'id_pelicula': self.id_pelicula,
            'titulo_pelicula': self.titulo_pelicula,
            'fecha_lanzamiento': self.fecha_lanzamiento.strftime('%Y-%m-%d'),
            'url_poster': self.url_poster
        }

    def __str__(self):
        '''Devuelve un string con la información de la película'''
        return f"{self.titulo_pelicula} ({self.fecha_lanzamiento.year})"

class Relacion:
    ''' Clase para manejar la información de una relación entre actores y películas '''
    def __init__(self, id_relacion, id_pelicula, id_estrella):
        self.id_relacion = int(id_relacion)
        self.id_pelicula = int(id_pelicula)
        self.id_estrella = int(id_estrella)
    def to_dict(self):
        ''' Devuelve un diccionario con la información de la relación '''
        return {
            'id_relacion': self.id_relacion,
            'id_pelicula': self.id_pelicula,
            'id_estrella': self.id_estrella
        }

class User:
    ''' Clase para manejar la información de un usuario '''
    def __init__(self, username, nombre_completo, email, password):
        self.username        = username
        self.nombre_completo = nombre_completo
        self.email           = email
        self.password        = password

    def to_dict(self):
        ''' Devuelve un diccionario con la información del usuario '''
        return {
            'username': self.username,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'password': self.password,
            'admin': self.admin
        }

    def hash_string(self, string):
        ''' Devuelve un hash de un string '''
        return hashlib.sha256(string.encode()).hexdigest()

class SistemaCine:
    ''' Clase para manejar la base de datos de peliculas'''
    def __init__(self):
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}

    def cargar_csv(self, archivo, clase):
        '''Carga los datos de un archivo CSV a la base de datos'''
        with open(archivo, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                obj = clase(**row)
                if clase == Actor:
                    actor = Actor(**row)
                    self.actores[actor.id_estrella] = actor
                elif clase == Pelicula:
                    pelicula = Pelicula(**row)
                    self.peliculas[pelicula.id_pelicula] = pelicula
                elif clase == Relacion:
                    relacion = Relacion(**row)
                    self.relaciones[relacion.id_relacion] = relacion
                elif clase == User:
                    user = User(**row)
                    self.usuarios[user.username] = user

    def obtener_peliculas_por_actor(self, id_estrella):
        ''' Devuelve una lista de peliculas en las que ha participado un actor '''
        id_peliculas = [rel.id_pelicula for rel in self.relaciones.values() if rel.id_estrella == id_estrella]
        return [self.peliculas[id_pelicula] for id_pelicula in id_peliculas]

if __name__ == '__main__':
    archivo_actores = "datos/actores.csv"
    archivo_pelis = "datos/peliculas.csv"
    archivo_relaciones = "datos/relacion.csv"
    archivo_usuarios = "datos/users.csv"
    sistema = SistemaCine()
    sistema.cargar_csv(archivo_usuarios, User)
    sistema.cargar_csv(archivo_actores, Actor)
    sistema.cargar_csv(archivo_pelis, Pelicula)
    sistema.cargar_csv(archivo_relaciones, Relacion)
    actores = sistema.actores
    for id_estrella, actor in actores.items():
        print(f"{id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}")
    lista_peliculas = sistema.obtener_peliculas_por_actor(1)
    print("==== Peliculas en las que ha participado el actor: ====")
    for pelicula in lista_peliculas:
        print(pelicula)
