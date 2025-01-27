def Calcular_Y(x:float,m:float,b:float)->float:
    '''
    Calcula el valor de y en una linea recta
    x: valor de x
    m: pendiente
    b: interseccion de y
    regresa el valor de y
    '''
    return m*x+b

def main():
    m=2
    b=3
    x=5
    y= Calcular_Y(x,m,b)
    print(f'Para x={x}, y={y}')

if __name__ == '__main__':
    main()

def test_linea():
    '''
    Prueba de funcionamiento de calcular_Y
    '''
    y = Calcular_Y(0.0,2.0,3.0)
    return y

if __name__ == '__main__':
    if test_linea() == 3.0: 
        print('everything aight')
    else:
        print('sum went wrong')