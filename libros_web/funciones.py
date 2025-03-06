'''Archivo con las funciones necesarias de la Aplicacion Libro web'''

import csv

def leer_archivo_csv(archivo:str)->list:
    ''' Funcion que lee un archivo csv y lo convierte en una lista de diccionarios '''
    with open(archivo, 'r', encoding='utf8') as file:
        return [x for x in csv.DictReader(file)]

def crea_diccionario_titulos(lista:list)->dict:
    ''' Funcion que crea un diccionario con los titulos de los libros como clave y el resto de los datos como valores'''
    return {x['title']:x for x in lista}

def crea_diccionario(lista:list, llave:str)->dict:
    ''' Funcion que crea un diccionario con los titulos de los libros como clave y el resto de los datos como valores'''
    return {x[llave]:x for x in lista}

def busca_en_titulo(diccionario, palabra)-> list:
    ''' Busca palabra en titulo de la lista de diccionarios '''
    lista = []
    palabra = palabra.lower()
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            lista.append(libro)
    return lista

def busca_en_diccionario(diccionario:dict, palabra:str)-> list:
    ''' Busca palabra en llave de la lista de diccionarios '''
    lista = []
    palabra = palabra.lower()
    for llave, libro in diccionario.items():
        if palabra in llave.lower():
            lista.append(libro)
    return lista


if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = leer_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario_titulos(lista_libros)
    resultado = busca_en_diccionario(diccionario_libros, 'rebels')
    print(resultado)
    diccionario_autores = crea_diccionario(lista_libros,'author')
    resultado = busca_en_diccionario(diccionario_autores, 'sandra')
    print(resultado)