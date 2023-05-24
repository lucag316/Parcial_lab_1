# LAS FUNCIONES PRINCIPALES, OSEA LAS FUNCIONES QUE ESTAN EN EL MENU
import json
import csv
from funciones_secundarias import *

def cargar_csv(path: str) -> list:
    """
    Brief: Toma el archivo csv, lo  separa por lineas, crea una lista de diccionarios (cada insumo es un dict), itera la lista y en cada iteracion crea un diccionario. Reutiliza la funcion normalizar_datos()
    
    Parameters:
        path: str -> el path del cvs que quiero pasar
    
    Return: Devuelve la lista
    """
    if type(path) == type(str()):
        with open(path, "r", encoding="utf-8") as file:     # le pongo utf-8  porque  me tira  un error  "UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 2557: character maps to <undefined>"
            lista_lineas = []
            lista_insumos = []
            for linea in file:
                linea = linea.replace("\n", "")               
                lista_lineas = linea.split(",")
                insumo = {}
                insumo["id"] = lista_lineas[0]
                insumo["nombre"] = lista_lineas[1]
                insumo["marca"] = lista_lineas[2]
                insumo["precio"] = lista_lineas[3]
                insumo["caracteristicas"] = lista_lineas[4]
                #print(insumo)
                lista_insumos.append(insumo)
        lista_insumos = normalizar_datos(lista_insumos)
        return lista_insumos

def listar_cantidad_por_marcas(lista_insumos: list):
    """
    Brief: Muestra todas las marcas y la cantidad de insumos correspondientes a cada una
    
    Parameters:
        lista_insumos: list -> La lista de la que quiero ver los datos
    
    Return: No retorna, imprime
    """
    diccionario_cantidades_marcas = {}
    for insumo in lista_insumos:
        marca = insumo["marca"]
        if marca in diccionario_cantidades_marcas:
            diccionario_cantidades_marcas[marca] += 1
        else:
            diccionario_cantidades_marcas[marca] = 1
    for marca, cantidad in diccionario_cantidades_marcas.items():
        print(f"{marca}: {cantidad}")

def listar_insumos_por_marca(lista_insumos:list, clave: str):
    """
    Brief: Muestra, para cada marca, el nombre y precio de los insumos correspondientes.
    
    Parameters: 
        lista_insumos: list -> La lista que quiero utilizar
    
    Return: Imprime el nombre y el precio
    """
    if(type(lista_insumos) == type([]) and type(clave) == type("") and len(lista_insumos) > 0):
        lista_marcas = proyectar_clave(lista_insumos, clave)
        
        for marca in lista_marcas:
            print(f"\n{marca.upper()}:")
            for insumo in lista_insumos:
                if insumo[clave] == marca:
                    print("    Nombre: {0} | Precio: ${1}".format(insumo["nombre"], insumo["precio"]))
            print("-------------------------------------")
# AGREGAR BIEN LO DE LA CLAVE Y QUE NO SEA SOLO MARCA
def buscar_insumo_por_caracteristica(lista_insumos: list) -> list:
    """
    Brief: El usuario ingresa una caracteristica y se listan todos los insumos que tienen esa caracteristica
    
    Parameters:
        lista_insumos: list -> La lista en la que quiero buscar esa caracteristica
    
    Return: Devuelve la lista con los elementos que tienen esa caracteristica
            -1 si los parametros tienen algun error
            un mensaje si la caracteristica no existe
    """
    lista_con_la_carac = []
    flag_hay_carac = False
    
    if type(lista_insumos) == type([]) and len(lista_insumos) > 0:
        carac_ingresada = input("Ingrese una caracteristica: ").lower()
        
        for insumo in lista_insumos:
            if carac_ingresada in insumo["caracteristicas"]:
                flag_hay_carac = True
                lista_con_la_carac.append(insumo)
        if flag_hay_carac:
            retorno = lista_con_la_carac
        else:
            flag_hay_carac = True
            retorno = "ERROR, caracteristica invalida"
    else:
        retorno = "-1"
    
    return retorno  

def listar_insumos_ordenados(lista_insumos: list):
    """
    Brief: Muestra el ID, descripción, precio, marca y la primera característica de todos los productos, ordenados por marca de forma ascendente (A-Z) y, ante marcas iguales, por precio descendente.

    Parameters:
        lista_insumos: list -> Lista que quiero ordenar
        
    Return: No retorna, imprime
    """
    lista_ordenada = bubble_sort_dict(lista_insumos, "marca", "precio")
    for insumo in lista_ordenada:
        print("""Id: {0}
        Nombre: {1}
        Precio: ${2}
        Marca: {3}
        Primer caracteristica: {4}
---------------------------------------""". format(insumo["id"], 
                    insumo["nombre"], 
                    insumo["precio"], 
                    insumo["marca"], 
                    insumo["caracteristicas"][0], ))

def realizar_compras(lista_insumos: list):
    """
    Brief: va agregando los productos que el usuario desea a una lista y al final genera una factura en un archivo TXT. Reutiliza las funciones: encontrar_marca(), elegir_producto() y generar_factura_txt()
    
    Parameters: 
        lista_insumos: list -> La lista de insumos completa
        
    Return: no retorna, genera la factura en el archivo TXT con las compras realizadas
    """
    respuesta = "s"
    lista_compras = []
    total = 0
    
    while respuesta == "s":
        marca_ingresada = input("ingrese una marca: ").capitalize().strip()
        productos_encontrados = encontrar_marca(lista_insumos, marca_ingresada)
        
        if type(productos_encontrados) == type(str()):
            print(productos_encontrados)
            continue # vuelve a pedir la marca
        
        mostrar_lista_insumos(productos_encontrados)
        
        id_producto_elegido = input("Ingrese el ID del producto que desea: ").lower().strip()
        productos_encontrado = None
        
        for producto in productos_encontrados:
            if id_producto_elegido == str(producto["id"]).lower().strip():
                productos_encontrado = producto
                break
            
        if productos_encontrado is None:
            print("El ID ingresado no corresponde a un producto de la marca: {0}".format(marca_ingresada))
            continue #vuelve a pedir la marca
        
        cantidad_producto_elegido = int(input("Ingrese la cantidad: "))
        producto_elegido = elegir_producto(productos_encontrados, marca_ingresada, id_producto_elegido, cantidad_producto_elegido)
        
        if type(producto_elegido) == type({}):
            lista_compras.append(producto_elegido)
            total += float(producto_elegido["precio_total_del_producto"])
        
        respuesta = input("CONTINUAR: (s) \nFINALIZAR: (otra tecla) \nRespuesta: ")
        if respuesta != "s":
            break
        
    generar_factura_txt(lista_compras, total)

def guardar_en_formato_json(lista_insumos):
    """
    Brief: Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra "Alimento".
    
    Parameters:
        lista:insumos: list -> La lista  sobre la que  quiero actuar
    
    Return: No retorna
    """
    # puedo agregar un parametro, qeu diga, si pretty es True que me lo escriba en formato lindo, y si es False, que me lo escriba como venga (IDEAS QUE PUEDO AGREGAR)
    lista_nombre_alimento = []
    for insumo in lista_insumos:
        if "Alimento" in insumo["nombre"]:
            lista_nombre_alimento.append(insumo)
    
    with open(r"C:\Users\luca_\Desktop\Parcial_lab_1\Parcial_lab_1\Punto_7_pretty.json", "w") as file:    # quiero dejar un poco mas prolijo la parte de caracteristicas, pero no se como hacer, VERLO DESPUES
        json.dump(lista_nombre_alimento, file, indent=4, ensure_ascii=False)  #   primero el objeto(por ej, lista), despues en el archivo que quiero guardar, el indent es para dejar los espacios que quiero, el cuarto es separators, para separar por lo que quiero, ejemplo json.dump(lista_nombre_alimento, file, indent=4, separators = (", ", " : ")) le estoy diciendo que deje un espadio depues de cada coma
    print("JSON generado exitosamente")

def leer_desde_formato_json():
    """
    Brief: Permite mostrar un listado de los insumos guardados en el archivo JSON generado en la opción anterior.
    
    Parameters: No tiene

    Return: No retorna, imprime la lista 
    """
    with open(r"C:\Users\luca_\Desktop\Parcial_lab_1\Parcial_lab_1\Punto_7_pretty.json", "r") as file:  # lo de pretty aca puedo hacer lo mismo 
        lista = json.load(file)
    print("Lista de insumos guardados en el archivo JSON")
    mostrar_lista_insumos(lista)

def actualizar_precios(lista_insumos: list) -> list:
    """
    Brief:  Aumento todos los precios de la lista de diccionarios pasada por parametro. Reutiliza la funcion: aplicar_aumento()
    
    Parameters:
        lista_insumos: list -> La lista que deseo utilizar
        
    Return: Devuelve la lista con todos los precios aumentados
    """
    lista_con_aumento = list(map(aplicar_aumento, lista_insumos))
    
    with open(r"C:\Users\luca_\Desktop\Parcial_lab_1\Parcial_lab_1\Insumos_modificado.csv", "w", newline="") as archivo_csv:
        escribe = csv.writer(archivo_csv)
        escribe.writerow(["ID", "NOMBRE", "MARCA", "PRECIO", "CARACTERISTICAS"])
        for insumo in lista_con_aumento:
            escribe.writerow([insumo["id"], insumo["nombre"], insumo["marca"], insumo["precio"], insumo["caracteristicas"]])
    #return lista_con_aumento

def imprimir_menu():
    """
    Brief: Imprime un menu de opciones
    
    Parameters: No recibe ningun parametro
    
    Return: No retorna, Imprime el menu
    """
    print("""
        =========================================
            ***** MENU DE OPCIONES *****
        =========================================
        1- Cargar datos desde archivo
        2- Listar cantidad por marca
        3- Listar insumos por marca
        4- Buscar insumo por caracteristica
        5- Listar insumos ordenados
        6- Realizar compras
        7- Guardar en formato JSON
        8- Leer desde el formato JSON
        9- Actualizar precios
        10 Salir del programa
        =========================================
        """)