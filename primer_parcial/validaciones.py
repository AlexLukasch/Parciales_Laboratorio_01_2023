import re
def es_numerica(input:str)->bool:
    retorno = False
    if(input.isdigit() == True) or ((input.startswith('-') and input[1:].isdigit())):
        retorno = True
    return retorno

def get_int(mensaje:str, mensaje_error:str)->int:
    entrada = input(mensaje)
    while es_numerica(entrada) == False:
        entrada = input(mensaje_error)
    return int(entrada)

def es_flotante(valor)->bool:
    retorno = False
    partes = valor.split('.')  # Dividimos el valor en dos partes con el punto
    if len(partes) == 2:  # Verifico si el valor tiene una parte entera y una decimal
        parte_entera = partes[0]
        parte_decimal = partes[1]
        if (parte_entera.isdigit() == True and parte_decimal.isdigit() == True):
            retorno = True
    return retorno

def get_float(mensaje:str, mensaje_error:str)->float:
    entrada = input(mensaje)
    while es_flotante(entrada) == False:
        entrada = input(mensaje_error)
    return float(entrada)  
