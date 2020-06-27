def edad_permitida(edad):
    if edad <= 18:
        print('¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.')
    elif edad >18 and edad <30:
        print('Es un momento excelente para impulsar tu carrera.')
    else:
        print('Nunca es tarde para aprender ¿Qué curso tomaremos?')

if __name__ == '__main__':
    try:
        edad = int(input('¿Que edad tienes?: '))
        edad_permitida(edad)
    except:
        print('Ingresa tu edad como numero, no palabras')

    