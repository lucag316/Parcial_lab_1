# LAS FUNCIONES PRINCIPALES, OSEA LAS FUNCIONES QUE ESTAN EN EL MENU

def cargar_csv(path: str) -> list:
    """
    Brief: Toma el archivo csv, lo  separa por lineas, crea una lista de diccionarios (cada insumo es un dict), itera la lista y en cada iteracion crea un diccionario
    
    Parameters:
        path: str -> el path del cvs que quiero pasar
    
    Return: Devuelve la lista
    """
    if type(path) == type(str()):
        with open(path, "r", encoding="utf-8") as file:     # le pongo utf-8  porque  me tira  un error  "UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 2557: character maps to <undefined>"
            lista_lineas = []
            lista_caracteristicas = []
            lista_insumos = []
            for linea in file:
                linea = linea.replace("\n", "")               
                lista_lineas = linea.split(",")
                lista_caracteristicas = lista_lineas[4].split("~")
                insumo = {}
                insumo["id"] = lista_lineas[0]
                insumo["nombre"] = lista_lineas[1]
                insumo["marca"] = lista_lineas[2]
                insumo["precio"] = lista_lineas[3]
                insumo["caracteristicas"] = lista_caracteristicas
                #print(insumo)
                lista_insumos.append(insumo)
        return lista_insumos







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