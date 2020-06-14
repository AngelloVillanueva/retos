def suma(numero_1,numero_2):
    resultado = numero_1 +numero_2
    print(resultado)

def suma_multiplicacion(numero_1,numero_2,numero_3):
    resultado_2 = (numero_1+numero_2)*numero_3
    print(resultado_2)

if __name__ == '__main__':
    numero_1 = float(input('Escribe el primer numero: '))
    numero_2 = float(input('Escribe el segundo numero: '))
    numero_3 = float(input('Escribe el tercer numero: '))
    suma(numero_1,numero_2)
    suma_multiplicacion(numero_1,numero_2,numero_3)
