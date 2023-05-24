import os
from funciones_principales import *
from funciones_secundarias import *

def menu_principal():
    """
    Brief: En esta funcion puedes ingresar una opcion y va a hacer lo que diga la opcion
    
    Parameters: No tiene parametros
    
    Return: No retorna, hace algo, segun la opcion que ingrese
    """
    flag_cargar_csv = False
    opciones_validas = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    os.system("cls")
    
    while True:
        imprimir_menu()
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            lista_insumos = cargar_csv(r"C:\Users\luca_\Desktop\Parcial\Parcial-lab-1\insumos.csv")
            flag_cargar_csv = True
            lista_copiada = copiar_lista(lista_insumos)
            #mostrar_lista_insumos(lista_insumos) 
        elif opcion in opciones_validas:
            if flag_cargar_csv:
                if opcion == "2":
                    listar_cantidad_por_marcas(lista_copiada)
                elif opcion == "3":
                    listar_insumos_por_marca(lista_copiada, "marca")
                    pass
                elif opcion == "4":
                    lista_segun_carac = buscar_insumo_por_caracteristica(lista_copiada)
                    mostrar_lista_insumos(lista_segun_carac)
                    pass
                elif opcion == "5":
                    listar_insumos_ordenados(lista_copiada)
                    pass
                elif opcion == "6":
                    realizar_compras(lista_copiada)
                    pass
                elif opcion == "7":
                    guardar_en_formato_json(lista_copiada)
                    pass
                elif opcion == "8":
                    leer_desde_formato_json()
                    pass
                elif opcion == "9":
                    actualizar_precios()
                    pass
                elif opcion == "10":
                    confirmacion = input("Esta seguro que quiere salir?\n(s) SALIR \n(otra tecla) CANCELAR \nRespuesta: ")
                    if confirmacion == "s":
                        break
                    else: 
                        pass
            else:
                print("Primero debes elegir la opcion 1 para cargar la lista")
        else:
            print("ERROR, La opcion no se encuentra en el menu")
        os.system("pause")

menu_principal()



# 4 MEJORAR COMO SE VE, mostrar_insumo
# 6 cuando ingreso una marca,  hacer que se vean mejor
# 7 se me queda guardada la lista como la modifique si ya la use, creo que tengo que usar una copia para los demas puntos
# 8 cuando lo leo hacer que  se vea mas lindo
