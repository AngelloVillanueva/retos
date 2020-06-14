def name():
    nombre = str(input('¿Cual es tu nombre?: '))
    apellido = str(input('¿Cual es tu Apellido?: '))
    edad = int(input('¿Cual es tu edad: '))
    edad_ap = edad -1 
    edad_pa = edad +1
    
    print('Hola, {} {}, el año pasado tenias {} años y el próximo cumpliras {} años'.format(nombre, apellido, edad_ap, edad_pa))
    print('Platzi cuenta con cursos de: \nDesarrollo e Ingenieria\nMarketing \nDiseño y UX \nNegocios y emprendimiento \nProducción Audiovisual \nCrecimiento profesional')
    

if __name__=='__main__':
    name()
