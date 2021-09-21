"""
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
    print("6- Transportar obras de un departamento ")
    print("7- Crear nueva exposición")

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
        identificador = 1
        
        info = controller.llamarArtistas(datos, anho_inicial, anho_final, tipo_lista)
        info_ordenada = controller.llamarInsertion(info, identificador)
        
        lista_final = info_ordenada[1]
        tiempo = info_ordenada[0]
        
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
        fecha_inicial_texto = input('Escriba la fecha inicial: ')
        fecha_inicial = datetime.strptime(fecha_inicial_texto, '%Y-%m-%d')
        fecha_final_texto = input('Escriba la fecha final: ')
        fecha_final = datetime.strptime(fecha_final_texto, '%Y-%m-%d')
        datos = lt.subList(catalogo['obras'], 1, len(catalogo['obras']['elements']))
        datos = datos.copy()
        identificador = 3
        #print(catalogo['obras'])
        
        resultado = controller.llamarQuicksort(datos, identificador)   
        
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
        identificador = 2
        nombreArtista = input('Escriba el nombre del artista a consultar: ')
        
        idArtista = controller.llamarConsultarId(datos, nombreArtista)      
        listaFiltradaPorId = controller.llamarFiltrarObrasPorId(datos, idArtista, tipo_lista)
        print(listaFiltradaPorId)
        listaOrdenadaDeObras = controller.llamarInsertion(listaFiltradaPorId[0], identificador)
        
        mayor = 0
        tecnica_mayor = None
        
        for i in listaFiltradaPorId[2]:
            cuant = listaFiltradaPorId[1].count(i)
            if cuant > mayor:
                mayor = cuant
                tecnica_mayor = i
                
        print("Clasificando ...")       
        print(('{} con MOMA Id {} tiene {} obras a su nombre en el museo.').format(nombreArtista, idArtista, listaFiltradaPorId[0]['size']))
        print(('Existen {} medios/técnicas diferentes en su trabajo.').format(len(listaFiltradaPorId[2])))
        print('Su técnica más utilizada es {} con {} obras.'.format(tecnica_mayor, mayor))    
              
        for i in listaFiltradaPorId[0]['elements']:
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
        
        print('La lista de nacionalidades ordenadas por el total de obras de mayor a menor (TOP 10) es :')
        print(' ')
        print(lista[0:10])
        print(' ')
        print(f'Las primeras 3 obras de nacionalidad {nacionalidad}')
        print(lista_obras['elements'][0])
        print(lista_obras['elements'][1])
        print(lista_obras['elements'][2])
        print(' ')
        print(f'Las ultimas 3 obras de nacionalidad {nacionalidad}')
        print(lista_obras['elements'][len(lista_obras['elements'])-3])
        print(lista_obras['elements'][len(lista_obras['elements'])-2])
        print(lista_obras['elements'][len(lista_obras['elements'])-1])
        input()
        system("cls")
        
    elif (inputs[0]) == 6:
        
        pass
    
    elif (inputs[0]) == 7:
        
        datos = catalogo.copy()
        anhoInicial = int(input("Digite el año inicial: "))
        anhoFinal = int(input("Digite el año final: "))
        areaDisponible = float(input("Digite el área disponible en m^2: "))
        
        rangoObrasRequerido = controller.llamarObtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista)
        nuevaExposicion = controller.llamarCrearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista)
        
        print('El MoMA va a exhibir piezas desde {} hasta {}'.format(anhoInicial, anhoFinal))
        print('Hay {} posibles piezas para un área de {} m^2 '.format(len(rangoObrasRequerido['elements']), areaDisponible))
        print('La posible exhibición tiene {} piezas'.format(len(nuevaExposicion[0]['elements'])))
        print('Se ocuparon {} m^2 de los {} m^2 disponibles'.format(nuevaExposicion[1], areaDisponible))
        print('Las primeras 5 obras: ')
         
        for i in nuevaExposicion[0]['elements'][:5]:
            print(i)
            
        print('Las últimas 5 obras: ')
        
        for i in nuevaExposicion[0]['elements'][(len(nuevaExposicion[0]['elements']) - 4):]:
            print(i)
            
        print('Toda la exposición completa se muestra a continuación: ')
        
        for i in nuevaExposicion[0]['elements']:
            print(i)        
        

    else:
        system("cls")
        sys.exit(0)
sys.exit(0)
