def flim(li,ls,comp):
    if comp>li and comp<ls:
        print(f'El numero {comp} esta dentro del limite, gracias')
    elif comp < li:
        print(f'El numero {comp} esta debajo del limite Inferior')
    else:
        print(f'El numero {comp} esta por encima del limite superior')

if __name__ == '__main__':
    try:
        li = float(input('Ingresa el numero limite Inferior: '))
        ls = float(input('Ingresa el numero limite Superior: '))
        comp = float(input('Ingresa el numero a comparar: '))
        sw = 0
        if li > ls:
            sw = ls
            ls = li
            li = sw
            print('Hemos cambiado el Limite inferio por el superior pues no correspondian')
            flim(li,ls,comp)
        else:
            flim(li,ls,comp)

    except ValueError:
        print('Error, ingresa un numero valido')