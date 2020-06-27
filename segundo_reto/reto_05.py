def clima(r):
    if r == "si":
        viento = str(input('¿Esta corriendo viento? (Si/No): ')).lower()
        if viento == 'si':
            print('No es recomendable usar sombrilla')
        else:
            print('Recuerda llevar una sombrilla!')
    else:
        print('Ten un bonito día!')

if __name__ == '__main__':
    r = str(input('¿Esta lloviendo?(Si/No): ')).lower()
    clima(r)
    
