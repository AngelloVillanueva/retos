def f_limite(limite,comparador):
    if comparador <= limite:
        print(f'El numero {comparador} esta dentro del limite, gracias')
    else:
        print(f'El numero {comparador} no esta dentro del limite')

if __name__ == '__main__':
    try:
        limite = float(input('Ingresa el numero limite: '))
        comparador = float(input('Intgesa el numero a comparar: '))
        f_limite(limite,comparador)
    except ValueError:
        print('Error, ingresa un numero valido')