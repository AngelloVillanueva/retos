def daytohours(days):
    hours = days*24
    minute = hours*60
    seconds = minute *60
    
    print(f'En {days} días hay {hours} horas, {minute} minutos y {seconds} segundos')


if __name__ == '__main__':
    hours=0
    minute=0
    seconds=0
    try:
        print('Transforma dias en horas, minutos y segundos')
        days = int(input('Ingresa el numero de días: '))
        daytohours(days)
    except ValueError:
        print('****************ERRROR***************')
        print('Ingresa solamente numeros en los dias')