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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def initCatalogo(tipo_lista):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalogo = model.crearCatalogo(tipo_lista)
    return catalogo

# Funciones para la carga de datos

def cargarDatos(catalogo):
    cargarArtistas(catalogo)
    cargarObras(catalogo)

def cargarArtistas(catalogo):
    archivoArtistas=cf.data_dir + 'Artists-utf8-small.csv'
    #archivoArtistas='D:\Descargas\Repositorio GitHub\Reto1-G07\Data\Artists-utf8-small.csv'
    input_file=csv.DictReader(open(archivoArtistas, encoding='utf8'))
    for artista in input_file:
        #print(artista)
        model.agregarArtista(catalogo, artista)
        
        
    

def cargarObras(catalogo):
    archivoObras=cf.data_dir + 'Artworks-utf8-small.csv'
    input_file=csv.DictReader(open(archivoObras, encoding='utf8'))
    for obra in input_file:
        model.agregarObra(catalogo, obra)

# Funciones de ordenamiento

def llamarInsertion(datos):
    resultado = model.insertion(datos)
    return resultado

def llamarShell(datos):
    resultado = model.shell(datos)
    return resultado

def llamarMerge(datos):
    resultado = model.merge(datos)
    return resultado

def llamarQuicksort(datos):
    resultado = model.quicksort(datos)
    return resultado

# Funciones de consulta sobre el catálogo
