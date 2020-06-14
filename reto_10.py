def convertirmillas(millas):
    kilometros = millas * 1.609344
    print(f'Las {millas} millas son {kilometros} km')

if __name__ == '__main__':
    try:
        print('*** C O N V I E R T E  M I L L A S ***')
        millas = float(input('Ingresa tus millas!: '))
        convertirmillas(millas)
    except ValueError:
        print('******** E R R O R *********\nIngresa solamente valores numericos')