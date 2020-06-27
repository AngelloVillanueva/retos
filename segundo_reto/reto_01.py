def mayormenor(num_1,num_2):
    if num_1 == num_2:
        print(f'{num_1} y {num_2} son iguales')
    elif num_1 > num_2:
        print(f'{num_1} es mayor que {num_2}')
    else:
        print(f'{num_1} es menor que {num_2}')

if __name__ == '__main__':
    try:
        num_1 = float(input('Escribe el un numero: '))
        num_2 = float(input('Escribe el segundo numero: '))
        mayormenor(num_1,num_2)
    except ValueError:
        print('*******************************')
        print('Error, ingresa un número valido')