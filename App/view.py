﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
from os import system
from datetime import date, time, datetime
from App import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

x = 1

def printMenu():
    system("cls")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronólógica de los artistas")
    print("3- Lista cronológica de las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")

catalogo = None

def initCatalogo():
    """
    Inicializa el catalogo del modelo
    """
    return controller.initCatalogo()

def cargarDatos(catalogo):
    """
    Carga las obras y los artistas en la estructura de datos
    """
    controller.cargarDatos(catalogo)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("1- ARRAY_LIST")
        print("2- LINKED_LIST")
        seleccion_tipo_lista = int(input("Seleccione el tipo de lista: "))
        
        if seleccion_tipo_lista == 1:
            tipo_lista = 'ARRAY_LIST'
            
        elif seleccion_tipo_lista == 2:
            tipo_lista = 'LINKED_LIST'
            
        print("Cargando información de los archivos ....")
        catalogo = controller.initCatalogo(tipo_lista)
        cargarDatos(catalogo)
        system("cls")
        

    elif int(inputs[0]) == 2:
        
        anho_inicial = int(input('Digite un año inicial: '))
        anho_final = int(input('Digite un año final: '))        
        datos = catalogo.copy()
        
        info = controller.llamarArtistas(datos, anho_inicial, anho_final, tipo_lista)
        info_ordenada = controller.llamarOrdenarArtistasPorNacimiento(info)
        
        lista_final = info_ordenada[1]
        tiempo = info_ordenada[0]
        
        #print(info)
        
        primeros_3 = lista_final['elements'][:3]
        ultimos_3 = lista_final['elements'][(len(lista_final['elements'])-2):]
        primeros_ultimos = primeros_3 + ultimos_3
        resultado_1 = 'Hay {} artistas nacidos entre {} y {}'.format(len(lista_final['elements']), anho_inicial, anho_final)
        
        print("Creando lista ....")
        print(resultado_1)
        print('=========================================================')
        print('Los primeros y los últimos 3 son: ')
        print(primeros_ultimos)
        print('=========================================================')
        print('La información de los artistas: ')
        
        for i in lista_final['elements']:
            print(i)
            
        print('El tiempo de ejecución fue de: ', tiempo, ' s.')

        input()
        system("cls")


    elif int(inputs[0]) == 3:
        #tamanho_muestra = int(input('Escriba el tamaño de la muestra que quiere analizar: '))
        fecha_inicial_texto = input('Escriba la fecha inicial: ')
        fecha_inicial = datetime.strptime(fecha_inicial_texto, '%Y-%m-%d')
        fecha_final_texto = input('Escriba la fecha final: ')
        fecha_final = datetime.strptime(fecha_final_texto, '%Y-%m-%d')
        datos = lt.subList(catalogo['obras'], 1, len(catalogo['obras']['elements']))
        datos = datos.copy()
        #print(catalogo['obras'])
        
        resultado = controller.llamarQuicksort(datos)   
        
        print("Creando lista ....")   
        dic=resultado[1]
        lista=dic['elements']
        lista_rango=lt.newList('ARRAY_LIST')
        
        for elemento in lista:
            if elemento['fecha_adquisicion']=='':
                pass
            else:
                fecha_elemento=datetime.strptime(elemento['fecha_adquisicion'], '%Y-%m-%d')
                if fecha_elemento > fecha_inicial and fecha_elemento < fecha_final:
                  lt.addLast(lista_rango, elemento)

        dic1=lista_rango['elements']
        numero_elementos=len(dic1)
        print("El número total de obras adquiridas por compra es de : " + str(controller.obrasAdquiridasPorCompra(datos)))
        print('El número de elementos en el rango es: ' + str(numero_elementos))
        print(' ')
        print('Los tres primeros elementos son:')
        print(dic1[0])
        print(dic1[1])
        print(dic1[2])
        print('')
        print('Los tres últimos elementos son:')
        print(dic1[numero_elementos-3])
        print(dic1[numero_elementos-2])
        print(dic1[numero_elementos-1])
        print(' ')

        input()
        system("cls")
        
        #print("Para la muestra de", tamanho_muestra, " elementos, el tiempo (mseg) es: ", str(resultado[0]))   
        
    
    elif int(inputs[0]) == 4:
        
        datos = catalogo.copy()
        nombreArtista = input('Escriba el nombre del artista a consultar: ')
        
        idArtista = controller.llamarConsultarId(datos, nombreArtista) 
        print(idArtista)     
        listaFiltradaPorId = controller.llamarFiltrarObrasPorId(datos, idArtista, tipo_lista)
        listaOrdenadaDeObras = controller.llamarOrdenarObras(listaFiltradaPorId[0])
        
        mayor = 0
        tecnica_mayor = None
        
        for i in listaFiltradaPorId[2]:
            cuant = listaFiltradaPorId[1].count(i)
            if cuant > mayor:
                mayor = cuant
                tecnica_mayor = i
                
        print("Clasificando ...")       
        print(('{} con MOMA Id {} tiene {} obras a su nombre en el museo.').format(nombreArtista, idArtista, len(listaFiltradaPorId[0])))
        print(('Existen {} medio/técnicas diferentes en su trabajo.').format(len(listaFiltradaPorId[2])))
        print('Su técnica más utilizada es {} con {} obras.'.format(tecnica_mayor, mayor))    
              
        for i in listaFiltradaPorId[0]:
            print(i)
        
        input()
        system("cls")
        
    
    elif int(inputs[0]) == 5:

        datos = catalogo.copy()
        print("Clasificando ...")
        lista = controller.llamarListaNacionalidades(datos)
        nacionalidad = lista[0][0]
        lista_obras = controller.llamarBuscarObrasPorNacionalidad(datos, nacionalidad)
        cont = 0
        print(f'Las primeras 20 obras de nacionalidad {nacionalidad}')
        for i in lista_obras['elements']:
            while cont < 20:
                print(f'Obra de nacionalidad {nacionalidad}: {i}')
                print(' ')
                cont = cont + 1
        
        print('La lista de nacionalidades ordenadas por el total de obras de mayor a menor (TOP 10) es :')
        print(' ')
        print(lista[0:10])
        input()
        system("cls")

    else:
        system("cls")
        sys.exit(0)
sys.exit(0)
