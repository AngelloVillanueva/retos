def mensaje(n):
    if n==1:
        print('Hoy aprenderemos sobre prorgamación')
    elif n==2:
        print('¿Qué tal tomar un curso de marketing digital?')
    elif n==3:
        print('Hoy es un gran día para comenzar a aprender de diseño')
    elif n==4:
        print('¿Y si aprendemos algo de negocios online?')
    elif n==5:
        print('Veamos un par de clases sobre producción audiovisual')
    elif n==5:
        print('Tal vez sea bueno desarrollar una habilidad blanda en Platzi')
    else:
        print('Elegiste un numero fuera de rango')

if __name__ == '__main__':
    try:
        n= int(input('Eligue un numero del 1 al 6: '))
        mensaje(n)
    except:
        print('Solo eligue un numero del 1 al 6, no palabras u otro numeros')
    