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
import operator
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
    artista = nuevoArtista(artista['ConstituentID'],artista['DisplayName'],artista['BeginDate'],artista['EndDate'],artista['Nationality'], artista['Gender'])
    lt.addLast(catalogo['artistas'], artista)

def agregarObra(catalogo, obra):
    obra=nuevaObra(obra['ConstituentID'], obra['ObjectID'], obra['Title'], obra['Date'], obra['Medium'], obra['Department'], obra['DateAcquired'], obra['Height (cm)'], obra['Width (cm)'], obra['Weight (kg)'], obra['CreditLine'], obra['Dimensions'])
    lt.addLast(catalogo['obras'], obra)

# Funciones para creacion de datos

def nuevoArtista(id, nombre, fecha_nacimiento, fecha_muerte, nacionalidad, genero):
    artista={'id':"", 'nombre':"", 'fecha_nacimiento':"", 'fecha_muerte':"", 'nacionalidad':"", 'genero':""}
    artista['id'] = id
    artista['nombre']=nombre
    artista['fecha_nacimiento'] = fecha_nacimiento
    artista['fecha_muerte'] = fecha_muerte
    artista['nacionalidad']=nacionalidad
    artista['genero'] = genero
    #artista['obras']=lt.newList('ARRAY_LIST')
    return artista

def nuevaObra(id, objectId, titulo, fecha, tecnica, departamento, fecha_adquisicion, altura, ancho, peso, linea, dimensiones):
    
    obra={'id':"", 'objectId':"", 'titulo':"", 'fecha':"", 'tecnica':"", 'departamento':"", 'fecha_adquisicion':"", 'altura':"", 'ancho':"", 'peso':"", 'linea_adquisicion':"", 'dimensiones':""}
    obra['id']=id
    obra['objectId'] = objectId
    obra['titulo']=titulo
    obra['fecha']=fecha
    obra['tecnica']=tecnica
    obra['departamento']=departamento
    obra['fecha_adquisicion']=fecha_adquisicion
    obra['altura']=altura
    obra['ancho']=ancho
    obra['peso']=peso
    obra['linea_adquisicion']=linea
    obra['dimensiones'] = dimensiones
    
    return obra

# Funciones de consulta

def compararFechasArtistas(datos, anho_inicial, anho_final, tipo_lista):
    
    #listaArtistas = lt.getElement(datos['artistas'],0)
    #listaArtistas = datos['artistas']['elements']
    listaInfo = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['artistas']):
        
        if (int(i['fecha_nacimiento']) >= anho_inicial and int(i['fecha_nacimiento']) <= anho_final):
            lt.addLast(listaInfo, i)
    
    return listaInfo
            
        
def obrasAdquiridasPorCompra(datos):
    
    contador=0

    for dato in lt.iterator(datos):
        frase=dato['linea_adquisicion']
        if re.search('purchase',frase.lower()):
            contador=contador + 1

    return contador


def consultarId(datos, nombreArtista):
    
    idArtista = ""
    
    for i in lt.iterator(datos['artistas']):
        
        if i['nombre'] == nombreArtista:
            idArtista = i['id']
            break
        
    return idArtista      

def buscarObrasPorNacionalidad(datos, nacionalidad):
    info_obras = datos['obras']['elements']

    lista_obras = lt.newList('ARRAY_LIST')    

    for i in info_obras:

        x=i['id']
    
        characters = "[] "

        for s in range(len(characters)):
            x = x.replace(characters[s],"")

        lista = x.split(',')
        for j in lista:
            if consultarNacionalidad(datos, int(j)) == nacionalidad:
                lt.addLast(lista_obras, i)

    return lista_obras


    

def consultarNacionalidad(datos, id):

    info_artistas = datos['artistas']['elements']
    nacionalidad = ""

    for i in info_artistas:
        if i['id'] == str(id):
            nacionalidad = i['nacionalidad']
            break
        
    return nacionalidad 

def listaNacionalidades(datos):

    info_obras = datos['obras']['elements']

    lista_id_artistas = lt.newList('ARRAY_LIST')
    dic_nacionalidades = {}
    

    for i in info_obras:

        x=i['id']
    
        characters = "[] "

        for s in range(len(characters)):
            x = x.replace(characters[s],"")

        lista = x.split(',')
        #print(lista)
        for a in lista:
            if lt.isPresent(lista_id_artistas, a) == -1 or a == ' ' or a == '':
               pass
            else:
                lt.addLast(lista_id_artistas, a)

    inf=lista_id_artistas['elements']
    for i in inf:
        nacionalidad = consultarNacionalidad(datos, int(i))

        if nacionalidad in dic_nacionalidades:
            dic_nacionalidades[nacionalidad]=dic_nacionalidades[nacionalidad]+1
        else:
            dic_nacionalidades[nacionalidad]=1

    del dic_nacionalidades['']

    nacionalidades_sort = sorted(dic_nacionalidades.items(), key=operator.itemgetter(1), reverse=True)
    
    return nacionalidades_sort

def filtrarObrasPorId(datos, idArtista, tipo_lista):
    
    obrasDelArtista = lt.newList(tipo_lista)
    lista_temp_1 = []
    lista_temp_2 = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['obras']):
        
        tamanho_id = len(i['id'])
        if (str(i['id'][1:(tamanho_id-1)]) == idArtista):
            lt.addLast(obrasDelArtista, i)
            lista_temp_1.append(i['tecnica'])

            if (lt.isPresent(lista_temp_2, i['tecnica']) == 0):
                lt.addLast(lista_temp_2, i['tecnica'])
    
    return obrasDelArtista, lista_temp_1, lista_temp_2
          
    
def obtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista):
    
    info = datos['obras']['elements']
    rangoObras = lt.newList(tipo_lista)
    
    for i in info:
        if (('before' in i['fecha']) or ('Before' in i['fecha']) or ('December' in i['fecha']) or ('c.' in i['fecha'])):
            i ['fecha'] = i['fecha'][(len(i['fecha'])-4):] 
            print(i['fecha'])  
        elif i['fecha'] == 'Unknown':
            i['fecha'] = 0   
            print(i['fecha'])  
        elif '(November 11-14) 1963' == i['fecha']:
            i['fecha'] = 1963
            print(i['fecha']) 
        elif '(July 30-August 7) 1965' == i['fecha']:
            i['fecha'] = 1965
            print(i['fecha']) 
        elif '(October, 1985)' == i['fecha']:
            i['fecha'] = 1965
            print(i['fecha'])
        elif 'published November 1898' == i['fecha']:
            i['fecha'] = 1898
            print(i['fecha'])  
        elif (('-' in i['fecha']) and ('(' in i['fecha'])):
            i['fecha'] = i['fecha'][1:(len(i['fecha'])-6)]
            print(i['fecha']) 
        elif '-' in i['fecha']:
            if (i['fecha']).index('-') == 0:
                i['fecha'] = i['fecha'][1:]
            else:
                i['fecha'] = i['fecha'][:4]
            print(i['fecha'])
        elif '(newspaper published October 19, 1994 through March 14, 1995)' == i['fecha']:
            i['fecha'] = 1994
            print(i['fecha']) 
        
        
                        
        if ((int(i['fecha']) <= anhoFinal) and (int(i['fecha']) >= anhoInicial)):
            alturaObra = i['altura']
            anchoObra = i['ancho']
            
            print(i['fecha']) 
            
            if alturaObra == "":
                alturaObra = 0
            if anchoObra == "":
                anchoObra = 0
                
            i['areaObra'] = (((float(alturaObra))*(float(anchoObra))))*0.0001
            lt.addLast(rangoObras, i)    
            
    return rangoObras


def agregarArtistaPorId(datos, datosArtistas):
    
    for i in lt.iterator(datos):   
        for j in lt.iterator(datosArtistas):
            
            if (j['nombre'] != ""):
                if i['id'][1:-1] == j['id']:
                    i['artista'] = j['nombre']
            else:
                i['artista'] = 'Unknown'
   
    return datos
            
    
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
        lista_ordenada = ist.sort(datos, cmpArtworkByDateAcquired)
        
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
        lista_ordenada = sst.sort(datos, cmpArtworkByDateAcquired)
        
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
        lista_ordenada = mst.sort(datos, cmpArtworkByDateAcquired)

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
        lista_ordenada = qst.sort(datos, cmpArtworkByDateAcquired)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

#Otras
  
def crearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista):
    
    areaUsada = 0
    i = 0
    info = rangoObrasRequerido['elements']
    nuevaExposicion = lt.newList(tipo_lista)
    
    while ((areaUsada <= areaDisponible) and (i < (len(rangoObrasRequerido['elements'])))):
        
        areaUsada += info[i]['areaObra']
        lt.addLast(nuevaExposicion, info[i])
        
        i += 1
        
    return nuevaExposicion, areaUsada