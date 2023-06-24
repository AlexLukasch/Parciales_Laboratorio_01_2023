'''
Primer parcial de Laboratorio 1 Mayo 2023
Alexander Lukasch Belbey 1B
'''
from os import system
from validaciones import *
from funciones import *
system('cls')



while True:
    print("///////////////// MENU DE OPCIONES /////////////////\n"
          "1. Traer datos desde el archivo.\n"
          "2. Listar cantidad por raza.\n"
          "3. Listar personajes por raza.\n"
          "4. LListar personajes por habilidad.\n"
          "5. Jugar batalla.\n"
          "6. Guardar Json.\n"
          "7. Leer Json.\n"
          "8. Salir del programa.\n"
          "////////////////////////////////////////////////////")
    opcion = get_int("Elija una opcion para mostrar la información: ", "ERROR. Por favor ingrese una opción válida [NO LETRAS]:\n")
    
    match opcion:
        case 1:
            lista_personajes = []
            lista_personajes = parser_csv("D:\Parciales_Laboratorio_01_2023\primer_parcial\DBZ.csv")
            print(lista_personajes)
            convertir_strings_numeros(lista_personajes)
            normalizar_habilidades(lista_personajes)
            normalizar_raza(lista_personajes)
            confirmar_continuar()
        case 2:
            diccionario_razas = contar_elementos_por_clave(lista_personajes, "raza")
            print("Mostrando cantidad de personajes por raza: (Cuenta las 5 razas dobles)")
            mostrar_un_diccionario(diccionario_razas)
            confirmar_continuar()
        case 3:
            diccionario_razas = guardar_elementos_por_clave(lista_personajes, "raza")
            print("Mostrando cantidad de personajes por raza: (Cuenta las 5 razas dobles)")
            mostrar_un_diccionario(diccionario_razas)
            confirmar_continuar()
        case 4:
            diccionario_habilidad = guardar_elementos_por_clave(lista_personajes, "habilidades")
            print("Mostrando cantidad de personajes por raza: (Cuenta las 5 razas dobles)")
            mostrar_un_diccionario(diccionario_habilidad)
            confirmar_continuar()
        case 5:
            pass
            confirmar_continuar()
        case 6:
            pass
            confirmar_continuar()
        case 7:
            pass
            confirmar_continuar()
        case 8:
            print("Saliendo del programa...\n")
            break
        case other:
            print("Error, por favor ingrese una opción válida [DEL 1 AL 8]\n")
            confirmar_continuar()