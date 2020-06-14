def restar_pizzar(numero_rebanadas, rebanadas_comidas):
    quedan = numero_rebanadas - rebanadas_comidas
    print('Tenias {} rebanadas de pizza, te comiste {} y ahora te quedan {}'.format(numero_rebanadas,rebanadas_comidas,quedan))

    

if __name__=='__main__':
    try:
        numero_rebanadas = int(input('¿Cuantas rebanadas de pizza tienes?: '))
        rebanadas_comidas = int(input('¿Cuantas rebanadas de pizza te comiste?: '))
        restar_pizzar(numero_rebanadas, rebanadas_comidas)
    except ValueError:
        print('Recuerda solo ingresar números.')
