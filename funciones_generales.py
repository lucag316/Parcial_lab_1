# LAS FUNCIONES GENERALES, OSEA LAS QUE PUEDO USAR EN OTROS LUGARES( LE PUEDO PONER FUNCIONES SECUNDARIAS SINO)

def normalizar_datos(lista: list) -> list:
    """
    Brief: Normaliza los datos de la lista pasada por parametro
    
    Parameters:
        lista: list -> La lista que desea normalizar
        
    Return: La lista normalizada, imprime un mensaje en caso de error
    """
    lista_normalizada = []
    if len(lista) > 0:
        if type(lista) == type([]):
            for elemento in lista:
                id_normalizado = int(elemento["id"])
                nombre_normalizado = str(elemento["nombre"])
                marca_normalizada = str(elemento["marca"])
                precio_normalizado = float(elemento["precio"])
                caracteristicas_normalizadas = str(elemento["caracteristicas"])
                
                elemento_normalizado = {
                    "id": id_normalizado,
                    "nombre": nombre_normalizado,
                    "marca": marca_normalizada,
                    "precio": precio_normalizado,
                    "caracteristicas": caracteristicas_normalizadas
                    }
                lista_normalizada.append(elemento_normalizado)
        else:
            print("ERROR, el parametro no es de tipo lista")
    else:
        print("ERROR, la lista esta vacia")
    return lista_normalizada

def mostrar_insumo(insumo: dict):
    """
    Brief: muestra mas prolijo el insumo pasado por parametro, con las claves: id, nombre, marca, precio y caracteristicas
    
    Parameters: 
        insumo: dict -> El diccionario del insumo que quiero mostrar
    
    Return: Imprime el diccioonario, en caso de faltar alguna clave, imprime cual es la que falta
    """
    flag_claves_necesarias = True
    claves_necesarias = ["id", "nombre", "marca", "precio", "caracteristicas"]
    if type(insumo) == type({}):
        for clave in claves_necesarias:
            if clave not in insumo:
                flag_claves_necesarias = False
                print("La clave {0} no esta en el diccionario".format(clave))
        if flag_claves_necesarias:
            print("""
    --------------------------------------------------------------------------------------------
        Id: {0}
        Nombre: {1}
        Marca: {2}
        Precio: {3}
        Carcarteristicas: {4}
    --------------------------------------------------------------------------------------------
        """.format(insumo["id"], insumo["nombre"], insumo["marca"], insumo["precio"], insumo["caracteristicas"]).strip())
    else:
        print("ERROR, el parametro no es de tipo diccionario")

def mostrar_lista_insumos(lista_insumos: list):
    """
    Brief: Imprime la lista mas prolija. Reutiliza la funcion: mostrar_insumo()
    
    Parameters:
        lista_insumos: list -> La lista que quiero mostrar prolijamente
        
    Return: Imprime la lista mas prolija, o si sale algo mal imprime el error
    """
    if len(lista_insumos) > 0:
        if type(lista_insumos) == type([]):
            for insumo in lista_insumos:
                mostrar_insumo(insumo)
        else:
            print("ERROR, el parametro no es de tipo lista")
    else:
        print("ERROR, la lista esta vacia")

def bubble_sort_dict(lista: list, clave:str, flag_ascendente: bool = True) -> list:
    """
    Brief: Ordena la lista de diccionarios segun los parametros que le pases
    
    Parameters:
        lista: list -> La lista que quiero ordenar
        clave: str -> Por la  clave que lo quiero ordenar
        flag_ascendente: bool -> Por defecto esta en  True, si quiero de manera descendente poner False
    
    Return: Devuelve la lista que le pasaste pero ordenada segundo los parametros que le pasaste
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (flag_ascendente and lista[i][clave] > lista[j][clave]) or (flag_ascendente == False and lista[i][clave] < lista[j][clave]): # los mismo: not ascendente
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux                 # para mi hacer una funcion de copiar lista
    return lista                                    # no hace falta  retornar porque las listas son mutables, lo que pasa es que si primero hago esto, ya la lista original me cambio y queda asi


