import os
from funciones import *
from funciones_generales import *

def menu_principal():
    """
    Brief: En esta funcion puedes ingresar una opcion y va a hacer lo que diga la opcion
    
    Parameters: No tiene parametros
    
    Return: No retorna, hace algo, segun la opcion que ingrese
    """
    os.system("cls")
    imprimir_menu()
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            lista_insumos = cargar_csv(r"C:\Users\luca_\Desktop\Parcial\Parcial-lab-1\insumos.csv")
            #mostrar_lista_insumos(lista_insumos)   # VER SI EN ESTA OPCION SOLO HAY QUE CARGARLA EN VEZ DE I
            pass
        elif opcion == "2":
            #listar_cantidad_por_marcas(lista_insumos)
            pass
        elif opcion == "3":
            listar_insumos_por_marca(lista_insumos, "marca")
            pass
        elif opcion == "4":
            lista_segun_carac = buscar_insumo_por_caracteristica(lista_insumos)
            mostrar_lista_insumos(lista_segun_carac)
            pass
        elif opcion == "5":
            #listar_insumos_ordenados(lista_insumos)
            pass
        elif opcion == "6":
            #realizar_compras()
            pass
        elif opcion == "7":
            #guardar_en_formato_json(lista_insumos)
            pass
        elif opcion == "8":
            #leer_desde_formato_json()
            pass
        elif opcion == "9":
            #actualizar_precios()
            pass
        elif opcion == "10":
            #lista_copiada = copiar_lista(lista_insumos) # sigue pasado lo mismo
            pass
            #print(lista_copiada)
        os.system("pause")

menu_principal()