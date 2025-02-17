'''
Main program for the game
'''
import string
import functions as fn
from random import choice
import unicodedata
import os
import argparse

def main(archivo_texto:str, nombre_plantilla='plantilla'):  
    '''
    Main
    '''
    #cargamos las plantillas
    plantillas = fn.carga_plantillas('plantillas')
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o>0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra')
            break
    print(f"La palabra era: {p}")
    fn.despliega_plantilla(plantillas, o)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('archivo', help='Archivo de texto con las palabras del juego', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print('El archivo no existe')
        exit()
    #archivo = './datos/pg15532.txt'
    main(archivo)