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
            
        print("Cargando información de los archivos ....")
        catalogo = controller.initCatalogo(tipo_lista = 'ARRAY_LIST')
        cargarDatos(catalogo)

        system("cls")
        

    elif int(inputs[0]) == 2:
        
        anho_inicial = int(input('Digite un año inicial: '))
        anho_final = int(input('Digite un año final: '))        
        datos = catalogo.copy()
        identificador = 1
        
        info = controller.llamarArtistas(datos, anho_inicial, anho_final, tipo_lista = 'ARRAY_LIST')
        info_ordenada = controller.llamarInsertion(info, identificador)      
        lista_final = info_ordenada[1]
        tiempo = info_ordenada[0]
        
        primeros_3 = lt.subList(lista_final, 1, 3)  
        ultimos_3 = lt.subList(lista_final, (lt.size(lista_final)-2), 3)  
        resultado_1 = 'Hay {} artistas nacidos entre {} y {}'.format(lt.size(lista_final), anho_inicial, anho_final)
        
        print(resultado_1)
        print('========================================================')
        
        print('Los primeros 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print(' ')  
        print('Los últimos 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print('==================================================================================================')    
        print('El tiempo de ejecución fue de: ', tiempo, ' ms.')

        input()
        system("cls")


    elif int(inputs[0]) == 3:
        
        fecha_inicial_texto = input('Escriba la fecha inicial: ')
        fecha_inicial = datetime.strptime(fecha_inicial_texto, '%Y-%m-%d')
        fecha_final_texto = input('Escriba la fecha final: ')
        fecha_final = datetime.strptime(fecha_final_texto, '%Y-%m-%d')
        datos = lt.subList(catalogo['obras'], 1, lt.size(catalogo['obras']))
        datos = datos.copy()
        identificador = 3
        resultado = controller.llamarQuicksort(datos, identificador)   
          
        dic=resultado[1]
        tiempo = resultado[0]
        datosArtistas = catalogo['artistas']
        
        
        
        dic_con_artista = controller.llamarAgregarArtistaPorId(dic, datosArtistas)
        print(dic)
        print('==========================================00')
        print(dic_con_artista)
        #lista=dic['elements']
        lista_rango=lt.newList('ARRAY_LIST')
        
        for elemento in lt.iterator(dic):
            if elemento['fecha_adquisicion']=='':
                pass
            else:
                fecha_elemento=datetime.strptime(elemento['fecha_adquisicion'], '%Y-%m-%d')
                if fecha_elemento > fecha_inicial and fecha_elemento < fecha_final:
                  lt.addLast(lista_rango, elemento)

        numero_elementos = lt.size(lista_rango)
        primeros_3 = lt.subList(dic_con_artista, 1, 3)
        ultimos_3 = lt.subList(dic_con_artista, (lt.size(dic_con_artista)-4), 3)
        #dic1=lista_rango['elements']
        #numero_elementos=len(dic1)
        print("El número total de obras adquiridas por compra es de : " + str(controller.obrasAdquiridasPorCompra(dic)))
        print('El número de elementos en el rango es: ' + str(numero_elementos))
        print(' ')
        print('Los tres primeros elementos son:')
        print('        Título         |    Artísta(s)    |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['titulo'], i['artista'], i['fecha'], i['tecnica'], i['dimensiones']))
        #print(dic1[0])
        #print(dic1[1])
        #print(dic1[2])
        print('')
        print('Los tres últimos elementos son:')
        #print(dic1[numero_elementos-3])
        #print(dic1[numero_elementos-2])
        #print(dic1[numero_elementos-1])
        print('        Título         |    Artísta(s)    |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['titulo'], i['artista'], i['fecha'], i['tecnica'], i['dimensiones']))
        print(' ')
        print('El tiempo de ejecución fue de: ', tiempo, ' ms.')

        input()
        system("cls")
        
        #print("Para la muestra de", tamanho_muestra, " elementos, el tiempo (mseg) es: ", str(resultado[0]))   
        
    
    elif int(inputs[0]) == 4:
        
        datos = catalogo.copy()
        identificador = 2
        nombreArtista = input('Escriba el nombre del artista a consultar: ')
        
        idArtista = controller.llamarConsultarId(datos, nombreArtista)      
        listaFiltradaPorId = controller.llamarFiltrarObrasPorId(datos, idArtista, tipo_lista = 'ARRAY_LIST')
        print(listaFiltradaPorId)
        listaOrdenadaDeObras = controller.llamarInsertion(listaFiltradaPorId[0], identificador)
        
        mayor = 0
        tecnica_mayor = None
        
        for i in lt.iterator(listaFiltradaPorId[2]):
            cuant = listaFiltradaPorId[1].count(i)
            if cuant > mayor:
                mayor = cuant
                tecnica_mayor = i
                
        print("Clasificando ...")       
        print(('{} con MOMA Id {} tiene {} obras a su nombre en el museo.').format(nombreArtista, idArtista, lt.size(listaOrdenadaDeObras[1])))
        print(('Existen {} medios/técnicas diferentes en su trabajo.').format(lt.size(listaFiltradaPorId[2])))
        print('Su técnica más utilizada es {} con {} obras.'.format(tecnica_mayor, mayor))    
        print('')   
        print('\tTítulo \t |Fecha de la obra|    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')      
        for i in lt.iterator(listaOrdenadaDeObras[1]):
            if i['tecnica'] == tecnica_mayor:
                print('{}\t   {} \t\t {} \t\t {}'.format(i['titulo'], i['fecha'], i['tecnica'], i['dimensiones']))
        print('')
        print('El tiempo de ejecución fue de: ', listaOrdenadaDeObras[0], ' ms.')
        
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
        
    elif (inputs[0]) == 6:
        
        pass
    
    elif int(inputs[0]) == 7:
        
        datos = catalogo.copy()
        anhoInicial = int(input("Digite el año inicial: "))
        anhoFinal = int(input("Digite el año final: "))
        areaDisponible = float(input("Digite el área disponible en m^2: "))
        
        rangoObrasRequerido = controller.llamarObtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista = 'ARRAY_LIST')
        nuevaExposicion = controller.llamarCrearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista = 'ARRAY_LIST')
        
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
