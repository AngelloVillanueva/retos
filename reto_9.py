resto = 0
resto_1 = 0
resto_2 = 0

def daytohours(days):
    resto = days % 24
    if resto == 0:
        hours = days // 24
    else:
        hours = days / 24
    print(hours)
        

if __name__ == '__main__':
    hours = 0
    try:
        print('Transforma dias en horas, minutos y segundos')
        days = int(input('Ingresa el numero de días: '))
    except ValueError:
        print('****************ERRROR***************')
        print('Ingresa solamente numeros en los dias')
    daytohours(days)
    