def name():
    nombre = str(input('¿Cual es tu nombre?: '))
    apellido = str(input('¿Cual es tu Apellido?: '))
    print('Hola, {} {}'.format(nombre, apellido))

    print('Platzi cuenta con cursos de: \nDesarrollo e Ingenieria\nMarketing \nDiseño y UX \nNegocios y emprendimiento \nProducción Audiovisual \nCrecimiento profesional')
    
if __name__=='__main__':
    name()
