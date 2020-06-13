def name():
    nombre = str(input('¿Cual es tu nombre?: '))
    apellido = str(input('¿Cual es tu Apellido?: '))
    print('Hola, {} {}'.format(nombre, apellido))

if __name__=='__main__':
    name()
