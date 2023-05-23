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
                nombre_normalizado = str(elemento["nombre"]).capitalize()
                marca_normalizada = str(elemento["marca"]).capitalize()
                precio_normalizado = str(elemento["precio"])
                precio_normalizado = float(precio_normalizado.replace("$", ""))
                caracteristicas_normalizadas = str(elemento["caracteristicas"]).lower().split("~")
                
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
        Id: {0}
        Nombre: {1}
        Marca: {2}
        Precio: ${3}
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


#-------------- 3
def esta_en_la_lista(lista: list, item: str) -> bool:
    """
    Brief: Te devuelve si el item esta o no esta en la lista de strings, NO de diccionarios
    
    Parameters:
        lista: list -> la lista de strings en la que se va a buscar
        item: str -> el item que se va a buscar en la lista
    
    Return: Si esta en la lista te retorna "True", si no esta "False", en caso de algun error, devuelve un mensaje
    """
    # intente validar que la lista no este vacia  pero para otras funciones no me serviria
    if type(lista) == type([]) and type(item) == type(""):
        flag_esta = False
        for elemento in lista:
            if elemento == item:
                flag_esta = True
                break
        retorno = flag_esta
    else:
        retorno = "ERROR, los datos pasados no son del tipo correcto"
    return retorno

def sacar_repetidos(lista: list) -> list:
    """
    Brief: Saca los repetidos de una lista de elementos basicos, NO de diccionarios- Reutiliza la funcion: esta_en_la_lista()
    
    Parameters:
        lista: list -> La lista que quiero sacarle los repetidos
    
    returns: Retorna una lista sin repetidos, o un mensaje en caso de error
    """
    #validar mejor por si pongo un numero por ejemplo
    if len(lista) > 0:
        if type(lista) == type([]):
            lista_sin_repetidos = []
            for elemento in lista:
                if not esta_en_la_lista(lista_sin_repetidos, elemento):
                    lista_sin_repetidos.append(elemento)
            retorno = lista_sin_repetidos
        else:
            retorno = "ERROR, los datos pasados no son del tipo correcto"
    else:
        retorno = "ERROR, la lista esta vacia"
    return retorno

def proyectar_clave(lista_insumos: list, clave: str, con_repe: bool = False) -> list:
    """
    Brief: Agrega una clave determinada de los diccionarios de la lista que le pasas a una lista nueva con solo esas claves, puede estar repetida o no, depende los parametros. Reutiliza la funcion: sacar_repetidos()
    
    Parameters:
        lista_insumos: list -> La lista de diccionarios que quiero filtrar
        clave: str -> La clave que quiero que sea la lista nueva
        con_repe: bool -> es opcional, si esta en "False" imprime sin repetida, si esta en "True" imprime con la clave repetida(predeterminado: False)
        
    Return: Retorna la lista filtrada
            -1 en caso de error
    """
    
    if type(lista_insumos) == type([]) and type(clave) == type("") and len(lista_insumos) > 0:
        lista_filtrada = []
        
        for insumo in lista_insumos:
            lista_filtrada.append(insumo[clave])
        
        if not con_repe:
            lista_filtrada = sacar_repetidos(lista_filtrada)
        
        retorno = lista_filtrada
    else:
        retorno = "-1"
    return retorno
#---------------- 3



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


#-------------------- 6
def encontrar_marca(lista_insumos: list, marca_ingresada: str) -> list:
    """
    Brief: Busca la marca que pases por parametro, en la lista pasada por parametro
    
    Parameters:
        lista_insumos: list -> La lista en la que quiero buscar
        marca_ingresada: str -> La marca que quiero buscar
        
    Return: Devuelve una lista con las marcas encontradas, si hay algun error devuelve un mensaje con dicho error
    """
    marcas_encontradas = []
    flag_marca_encontrada = False
    
    if len(lista_insumos) > 0:
        if type(lista_insumos) == type([]) and type(marca_ingresada) == type(str()):
            for producto in lista_insumos:
                marca = str(producto["marca"])
                
                if marca_ingresada.capitalize() == marca.capitalize().strip():
                    marcas_encontradas.append(producto)
                    retorno = marcas_encontradas
                    flag_marca_encontrada = True
            
            if not flag_marca_encontrada:
                retorno = f"No se encontro la marca: {marca_ingresada}"
        else:
            retorno = "ERROR, los datos pasados no son del tipo correcto"
    else:
        retorno = "ERROR, la lista esta vacia"
    return retorno

def elegir_producto(productos: list, marca_ingresada: str, id_producto_elegido: str, cantidad_producto_elegido: int) -> dict:
    """
    Brief: Elige el diccionario del producto que quiero de la lista pasada por parametro
    
    Parameters:
        productos: list -> La lista en la que voy a elegir el producto
        marca: str -> La marca ingresada por parametro por el usuario
        id_producto_elegido: str -> El ID del producto que quiero
        cantidad_producto_elegido: int -> La cantidad de unidades del producto
    
    Return: Devuelve un nuevo diccionario del producto elegido por el ID, caso contrario un mensaje si hay error
    """
    if len(productos) > 0:
        if type(productos) == type([]) and type(id_producto_elegido) == type(str()) and type(cantidad_producto_elegido) == type(int()):
            producto_elegido = None
            
            for producto in productos:
                if marca_ingresada.capitalize() == str(producto["marca"]).capitalize() and id_producto_elegido == str(producto["id"]).lower().strip():
                    producto_elegido = producto
                    break
            
            if producto_elegido:
                if cantidad_producto_elegido > 0 and cantidad_producto_elegido < 101:
                    producto_elegido["cantidad"] = cantidad_producto_elegido
                    producto_elegido["precio_total_del_producto"] = producto_elegido["precio"] * cantidad_producto_elegido
                    
                    return {"id": producto_elegido["id"],
                            "nombre": producto_elegido["nombre"],
                            "cantidad": producto_elegido["cantidad"],
                            "precio_por_unidad": producto_elegido["precio"],
                            "precio_total_del_producto":producto_elegido["precio_total_del_producto"]
                    }
                else:
                    return "cantidad no valida. Debe estar entre 1 y 100"
            else:
                return "ERROR, no se encontro un producto con la marca y el ID ingresados"
        else:
            return "ERROR, los datos pasados no son del tipo correcto"
    else:
        return  "ERROR, la lista esta vacia"

def generar_factura_txt(lista_compras: list, total: float):
    """
    Brief: Genera una factura de una compra segun la lista que se pase por parametro en un archivo TXT
    
    Parameters: 
        lista_compras: list -> La lista que quiero utilizar
        total: float -> El total de lo gastado en la lista de la compra
    
    Return: no retorna nada, imprime si se genero correctamente y escribe en el archivo TXT la factura 
    """
    with open(r"C:\Users\luca_\Desktop\Parcial\Parcial-lab-1\hola.txt", "w") as factura_txt:
        factura_txt.write("FACTURA DE LA COMPRA:\n")
        factura_txt.write("--------------------------------\n")
        
        for producto in lista_compras:
            factura_txt.write(f"Producto: {producto['nombre']}\n")
            factura_txt.write(f"Precio por unidad: ${producto['precio_por_unidad']}\n")
            factura_txt.write(f"Cantidad: {producto['cantidad']}\n")
            factura_txt.write(f"Precio total del producto: ${producto['precio_total_del_producto']}\n")
            factura_txt.write("--------------------------------\n")
            
        factura_txt.write(f"Total de la compra: ${total}")
        print("La factura se genero correctamente")
#-------------------- 6