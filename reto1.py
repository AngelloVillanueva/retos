def name():
    #Datos
    nombre = str(input('¿Cual es tu nombre?: '))
    apellido = str(input('¿Cual es tu Apellido?: '))
    
    #funciones de edad
    try:
        edad = int(input('¿Cual es tu edad?: '))
        edad_ap = edad -1 
        edad_pa = edad +1
    except ValueError:
        print('En la edad ingresa solo valores numericos')
    
    #Mostrar infromación
    print(f'Hola, {nombre} {apellido}, el año pasado tenias {edad_ap} años y el próximo cumpliras {edad_pa} años')

    print('Platzi cuenta con cursos de: \nDesarrollo e Ingenieria\nMarketing \nDiseño y UX \nNegocios y emprendimiento \nProducción Audiovisual \nCrecimiento profesional')
    

if __name__=='__main__':
    name()