def turtle(animal):
    if animal == 'tortuga':
        print('Tambien me gustan las tortugas')
    else:
        print('Ese animal es genial, pero prefiero las tortugas')

if __name__ == '__main__':
    animal = str(input('¿Cual es tu animal favorito?: ')).lower()
    turtle(animal)
    