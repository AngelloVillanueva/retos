def impuestos_por_pagar(cuenta,impuesto):
    iva = cuenta*(impuesto/100)
    print('*******************************')
    print(f'El impuesto es de {iva} pesos')

def divide_cuenta(cuenta, personas, propina):
    monto_propina = cuenta*(propina/100)
    totalpagar = cuenta + monto_propina
    cuenta_por_persona = totalpagar/personas
    print(f'La propina es de ${monto_propina} pesos\nEl total a pagar es de ${totalpagar} pesos\nPor lo que cada persona debe pagar ${cuenta_por_persona} pesos.')


if __name__=='__main__':
    cuenta = float(input('Ingresa el monto a pagar: $'))
    personas = float(input('Entre cuantas personas se dividira la cuenta: '))
    propina = float(input('Porcentaje de propina: '))
    impuesto = float(input('Cuanto es el impuesto: '))
    
    impuestos_por_pagar(cuenta,impuesto)
    divide_cuenta(cuenta, personas, propina)
