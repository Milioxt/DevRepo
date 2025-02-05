
import tablero

def main():
    '''
    Funcion principal
    '''
    numeros = [str(x) for x in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    g = tablero.juego(dsimbolos)
    if g is not None:
        print(f'Winner is {g}')
    else:
        print('Tie')


if __name__ == '__main__':
    main()