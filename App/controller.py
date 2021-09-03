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
 """

from DISClib.ADT import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def initCatalogo():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalogo = model.crearCatalogo()
    return catalogo

# Funciones para la carga de datos

def cargarDatos(catalogo):
    cargarArtistas(catalogo)
    cargarObras(catalogo)

def cargarArtistas(catalogo):
    archivoArtistas=cf.data_dir + 'Artists-utf8-small'
    input_file=csv.DictReader(open(archivoArtistas, encoding='utf8'))
    for artista in input_file:
        model.agregarArtista(catalogo, artista)

def cargarObras(catalogo):
    archivoObras=cf.data_dir + 'Artworks-utf8-small'
    input_file=csv.DictReader(open(archivoObras, encoding='utf8'))
    for obra in input_file:
        model.agregarObra(catalogo, obra)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
