def leap_year():
    Y = input("Ingrese un año: ")
    Y = int(Y)
    Y4 = Y % 4
    y100 = Y % 100
    Y400 = Y % 400
    if Y400 == 0:
        print(f'El año {Y} es bisiesto')
    elif Y4 == 0 and y100 != 0 :
        print(f'El año {Y} es bisiesto')
    else:
        print(f'El año {Y} no es bisiesto')
leap_year()
