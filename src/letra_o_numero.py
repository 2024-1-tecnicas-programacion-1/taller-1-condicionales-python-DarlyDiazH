def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    if caracter.isalpha():
        if caracter.isupper():
            return"Es letra Mayuscula"
        elif caracter.islower():
            return"Es letra Minuscula"
        elif caracter.isdigit():
            return"Es numero"
        else:
            print("No es letra ni número")


if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
