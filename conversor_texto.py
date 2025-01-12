def contar_vocales_consonantes(texto):
    vocales = 'aeiouAEIOU'
    n_vocales = sum(1 for c in texto if c in vocales)
    n_consonantes = sum (1 for c in texto if c.isalpha() and c not in vocales)
    return n_vocales, n_consonantes

while True:
    print('conversor de texto')
    texto = str(input('ingrese el texto: '))
    print('''1.convertir a mayusculas
        2.convertir a minusculas
        3.capitalizar
        4.contar vocales y consonantes
        5.salir''')
    
    opcion = int(input('escoja una opcion de las anteriores: '))

    #sentencia de flujo
    if opcion == 1:
        print(texto.upper())
    elif opcion == 2:
        print(texto.lower())
    elif opcion == 3:
        print(texto.capitalize())
    elif opcion == 4:
        resultado = print(contar_vocales_consonantes(texto))
    elif opcion == 5:
        print('saliendo del programa')
        break
    else:
        print('opcion invalida, seleccione una opcion valida')