'''
helpful func for the hangedman game
'''

def carga_archivo_texto(archivo:str)->list:
    '''
    loads a text file and gives back a list with the sentences of the file
    '''
    with open(archivo,'r',encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones


def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    loads the layout of the game thx to a txt file
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/template-ascci-{i}.txt')
    return plantillas

def despliega_plantillas(diccionario:dict, nivel:int):
    '''
    Displays a layout of THE GAME
    '''
    if nivel >=0 and nivel <=5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)


if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantillas(plantilla,0)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    print(lista_oraciones[110:115])
    texto = "".join(lista_oraciones[110:])
    print(texto[:110])