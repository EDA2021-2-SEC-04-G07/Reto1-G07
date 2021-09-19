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
import re
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
    artista = nuevoArtista(artista['ConstituentID'],artista['DisplayName'],artista['BeginDate'],artista['EndDate'],artista['Nationality'])
    lt.addLast(catalogo['artistas'], artista)

def agregarObra(catalogo, obra):
    obra=nuevaObra(obra['ConstituentID'], obra['Title'], obra['Date'], obra['Medium'], obra['Department'], obra['DateAcquired'], obra['Height (cm)'], obra['Width (cm)'], obra['Weight (kg)'], obra['CreditLine'])
    lt.addLast(catalogo['obras'], obra)

# Funciones para creacion de datos

def nuevoArtista(id, nombre, fecha_nacimiento, fecha_muerte, nacionalidad):
    artista={'id':"", 'nombre':"", 'fecha_nacimiento':"", 'fecha_muerte':"", 'nacionalidad':""}
    artista['id'] = id
    artista['nombre']=nombre
    artista['fecha_nacimiento'] = fecha_nacimiento
    artista['fecha_muerte'] = fecha_muerte
    artista['nacionalidad']=nacionalidad
    #artista['obras']=lt.newList('ARRAY_LIST')
    return artista

def nuevaObra(id, titulo, fecha, tecnica, departamento, fecha_adquisicion, altura, ancho, peso, linea):
    
    obra={'id':"", 'titulo':"", 'fecha':"", 'tecnica':"", 'departamento':"", 'fecha_adquisicion':"", 'altura':"", 'ancho':"", 'peso':"", 'linea_adquisicion':""}
    obra['id']=id
    obra['titulo']=titulo
    obra['fecha']=fecha
    obra['tecnica']=tecnica
    obra['departamento']=departamento
    obra['fecha_adquisicion']=fecha_adquisicion
    obra['altura']=altura
    obra['ancho']=ancho
    obra['peso']=peso
    obra['linea_adquisicion']=linea
    
    return obra

# Funciones de consulta

def compararFechasArtistas(datos, anho_inicial, anho_final, tipo_lista):
    
    listaArtistas = datos['artistas']['elements']
    listaInfo = lt.newList(tipo_lista)
    
    for i in listaArtistas:
        
        if (int(i['fecha_nacimiento']) >= anho_inicial and int(i['fecha_nacimiento']) <= anho_final):
            lt.addLast(listaInfo, i)
    
    return listaInfo
            
        
def obrasAdquiridasPorCompra(datos):
    contador=0

    for dato in datos['elements']:
        frase=dato['linea_adquisicion']
        if re.search('purchase',frase.lower()):
            contador=contador + 1

    return contador


def consultarId(datos, nombreArtista):
    
    info = datos['artistas']['elements']
    idArtista = ""
    encontro = False
    i = 0
    
    while not(encontro):
        
        if (info[i]['nombre'] == nombreArtista):
            idArtista = info[i]['id']
            encontro = True
            
        i += 1
        
    return idArtista     

def filtrarObrasPorId(datos, idArtista, tipo_lista):
    
    info_obras = datos['obras']['elements']
    obrasDelArtista = lt.newList(tipo_lista)
    lista_temp_1 = []
    lista_temp_2 = []
    mayor = None
    
    for i in info_obras:
        tamanho_id = len(i['id'])
        if (str(i['id'][1:(tamanho_id-1)]) == idArtista):
            lt.addLast(obrasDelArtista, i)
            lista_temp_1.append(i['tecnica'])
        
            if i['tecnica'] not in lista_temp_2:
                lista_temp_2.append(i['tecnica'])
    
    return obrasDelArtista, lista_temp_1, lista_temp_2
          
    
# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    
    if artwork1['fecha_adquisicion'] < artwork2['fecha_adquisicion']:
        return True
    else:
        return False
    
def cmpArtistaPorNacimiento(artista1, artista2):
    
    if int(artista1['fecha_nacimiento']) < int(artista2['fecha_nacimiento']):
        return True
    else:
        return False
    
def cmpObrasPorFecha(obra1, obra2):
    
    if (int(obra1['fecha']) < int(obra2['fecha'])):
        return True
    else:
        return False

# Funciones de ordenamiento

def insertion(datos, identificador): 
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = ist.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = ist.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada == ist.sort(datos, cmpArtworkByDateAcquired)
        
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def shell(datos, identificador):   
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = sst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = sst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada == sst.sort(datos, cmpArtworkByDateAcquired)
        
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def merge(datos, identificador):
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = mst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = mst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada == mst.sort(datos, cmpArtworkByDateAcquired)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def quicksort(datos, identificador):
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = qst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = qst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada == qst.sort(datos, cmpArtworkByDateAcquired)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

#Otras
        
    