'''
tablero.py Draws the board of the tiktaktoe game
'''
import random
def dibujar_tablero(simbolos:dict):

    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def juego(simbolos:dict):
    '''
    Juego del gato
    '''
    lista_combinaciones = [
        ['1'],['2'],['3'],
        ['4'],['5'],['6'],
        ['7'],['8'],['9'],
        ['1'],['4'],['7'],
        ['2'],['5'],['8'],
        ['3'],['6'],['9'],
        ['1'],['5'],['9'],
        ['3'],['5'],['7']
    ]




def ia(simbolos:dict):

    '''Juega la maquina'''
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''Juega el usuario'''
    lista_numeros = [str(i) for i in range(1,10)]
    ocupado = True
    while ocupado is True:
        x = input('Type the number u want to place the X in: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('U cant place there')
        else:
            print('Not a valid number')

def checa_winner(simbolos:dict, combinaciones:list):
    '''Checa si hay un ganador '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None




if __name__ =='__main__':
    numeros = [str(x) for x in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    dibujar_tablero(dsimbolos)
    ia(dsimbolos)
    dibujar_tablero(dsimbolos)
    usuario(dsimbolos)
    dibujar_tablero(dsimbolos)