import re
def confirmar_continuar():
    input("Presione enter para continuar...\n")

#Convierto string a enteros donde corresponde#
def convertir_strings_numeros(lista:list):
    for elemento in lista:
        elemento['id'] = int(elemento['id'])
        elemento['poder_pelea'] = int(elemento['poder_pelea'])
        elemento['poder_ataque'] = int(elemento['poder_ataque'])
#Parseo el archivo csv#
def parser_csv(path:str)->list:
    lista = []

    archivo = open(path, "r", encoding = "utf-8")
    for linea in archivo:
        lectura = re.split("[,\n]", linea)
        diccionario = {}
        diccionario["id"] = lectura[0]
        diccionario["nombre"] = lectura[1]
        diccionario["raza"] = lectura[2]
        diccionario["poder_pelea"] = lectura[3]
        diccionario["poder_ataque"] = lectura[4]
        diccionario["habilidades"] = lectura[5]
        lista.append(diccionario)
    archivo.close()
    return lista

def normalizar_habilidades(lista:list):
    for elemento in lista:
        elemento["habilidades"] = re.split("\\s+\|\$%|\|\$%", elemento["habilidades"])

def normalizar_raza(lista:list):
    for elemento in lista:
        elemento["raza"] = re.split("/", elemento["raza"])
        elemento["raza"] = tuple(elemento["raza"])
        print(elemento["raza"])
        #print(type(elemento["raza"]))

def contar_elementos_por_clave(lista:list, clave: str)->dict:
    diccionario_elementos = {}

    for elemento in lista:
        #print("///////////////////////////////////////////////////////////////")
        if(len(elemento[clave]) == 1):
            str(elemento[clave])
            if elemento[clave] in diccionario_elementos:
                diccionario_elementos[elemento[clave]] += 1 
            else:
                diccionario_elementos[elemento[clave]] = 1
        else:
            for sub_elemento in elemento[clave]:#Por cada raza en la tupla recorro
                for sub_dict in diccionario_elementos:
                    if sub_elemento in sub_dict:
                        diccionario_elementos[sub_dict] += 1 
    return diccionario_elementos

def guardar_elementos_por_clave(lista:list, clave: str)->dict:
    diccionario_elementos = {}
    for elemento in lista:
        if(len(elemento[clave]) == 1):
            #str(elemento[clave])
            print(elemento[clave])
            print(type(elemento[clave]))
            if elemento[clave] in diccionario_elementos:
                print(f"////ENTRO LA HABILIDAD: {elemento[clave]}/////////")
                diccionario_elementos[elemento[clave]] += ", " + elemento["nombre"]
            else:
                diccionario_elementos[elemento[clave]] = elemento["nombre"]
        else:
            for sub_elemento in elemento[clave]:#Por cada raza en la tupla recorro
                for sub_dict in diccionario_elementos:
                    if sub_elemento in sub_dict:
                        print(f"////ENTRO LA HABILIDAD: {elemento[clave]}/////////")
                        diccionario_elementos[sub_dict] += ", " + elemento["nombre"]
    return diccionario_elementos

def mostrar_un_diccionario(diccionario:dict):
    if (type(diccionario) == dict):
        for elemento in diccionario:
            print(f"{elemento[0]}: {diccionario[elemento]}")

def mostrar_una_key(lista:list, key:str, mensaje_key_1:str):
    if(type(lista) == list and len(lista)>0):
        for elemento in lista:
            tipo = type(elemento)
            print(f"{mensaje_key_1}{elemento[key]} TIPO: {tipo}")


