"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.Algorithms.Sorting import insertionsort as ist
from DISClib.Algorithms.Sorting import mergesort as mst
from DISClib.Algorithms.Sorting import quicksort as qst
from DISClib.Algorithms.Sorting import shellsort as sst
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def crearCatalogo(tipo_lista):
    """
    
    """
    catalogo = {'artistas': None,
                'obras': None,}

    catalogo['artistas'] = lt.newList(tipo_lista)
    catalogo['obras'] = lt.newList(tipo_lista)

    return catalogo


# Funciones para agregar informacion al catalogo

def agregarArtista(catalogo, artista):
    artista=nuevoArtista(artista[''],artista[''],artista[''])
    lt.addLast(catalogo['artistas'], artista)

def agregarObra(catalogo, obra):
    obra=nuevaObra(obra[''],obra[''],obra[''])
    lt.addLast(catalogo['obras'], obra)

# Funciones para creacion de datos

def nuevoArtista(nombre, fecha, nacionalidad):
    artista={'nombre':"",'fecha':"",'nacionalidad':"","obras": None}
    artista['nombre']=nombre
    artista['fecha']=fecha
    artista['nacionalidad']=nacionalidad
    artista['obras']=lt.newList('ARRAY_LIST')
    return artista

def nuevaObra(titulo, fecha, tecnica):
    obra={'titulo':"",'fecha':"",'tecnica':""}
    obra['titulo']=titulo
    obra['fecha']=fecha
    obra['tecnica']=tecnica
    return obra

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    
    if artwork1['DateAcquired'] < artwork2['DateAcquired']:
        return True
    else:
        return False

# Funciones de ordenamiento

def insertion(datos): 
    tiempo_inicial = time.process_time()
    lista_ordenada = ist.sort(datos, cmpArtworkByDateAcquired)
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def shell(datos):   
    tiempo_inicial = time.process_time()
    lista_ordenada = sst.sort(datos, cmpArtworkByDateAcquired)
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def merge(datos):
    tiempo_inicial = time.process_time()
    lista_ordenada = mst.sort(datos, cmpArtworkByDateAcquired)
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def quicksort(datos):
    tiempo_inicial = time.process_time()
    lista_ordenada = qst.sort(datos, cmpArtworkByDateAcquired)
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada