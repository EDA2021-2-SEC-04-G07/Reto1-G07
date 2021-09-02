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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def crearCatalogo():
    """
    
    """
    catalogo = {'artistas': None,
                'obras': None,}

    catalogo['artistas'] = lt.newList('SINGLE_LINKED')
    catalogo['obras'] = lt.newList('SINGLE_LINKED')

    return catalogo


# Funciones para agregar informacion al catalogo

def agregarArtista(catalogo, pArtista):
    cadArtista=pArtista.split(",")
    artista=nuevoArtista(cadArtista[1],cadArtista[5],cadArtista[3])
    lt.addLast(catalogo['artistas'], artista)

def agregarObra(catalogo, pObra):
    cadObra=pObra.split(",")
    obra=nuevaObra(cadObra[1],cadObra[3],cadObra[4])
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

# Funciones de ordenamiento