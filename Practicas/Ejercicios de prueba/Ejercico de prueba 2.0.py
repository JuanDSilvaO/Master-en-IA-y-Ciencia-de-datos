while True:
    try:
        nota  = float(input('Ingresa una nota (0 a 5): '))
        if 0 <= nota <= 5:
            print ('nota invalida:', nota)
            break
        else:
            print('fuera de rango. Intenta de nuevo')
    except ValueError:
        print('Entrada invalida. Ingresa un número')