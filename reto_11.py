def division(num_1,num_2):
    resultado = num_1/num_2
    print(f'{num_2} entra {resultado} veces en {num_1}')

if __name__ == '__main__':
    num_1 = float(input('Ingresa un numero mayor a 1000: '))
    num_2 = float(input('Ingresa un numero menor a 100: '))
    if num_1 >= 1000 and num_2 <=100:
        division(num_1,num_2)
    else:
        print('Los numeros no coinciden')