def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if (num_victorias_a > 6 and num_victorias_b < 5) or (num_victorias_b > 6 and num_victorias_a < 5):
         return "Invalido"
    elif num_victorias_a== 6 and num_victorias_b <= 4:
         return "Gano A"
    elif num_victorias_b == 6 and num_victorias_a <= 4:
         return "Gano B"
    elif (num_victorias_b == 5 and num_victorias_a == 7) or (num_victorias_b == 6 and num_victorias_a == 7):
         return "Gano A"
    elif (num_victorias_a == 5 and num_victorias_b == 7) or (num_victorias_a == 6 and num_victorias_b == 7):
         return "Gano B"
    elif num_victorias_a < 6 and num_victorias_b < 6:
         return "Aun no termina"
    elif (num_victorias_a == 6 and num_victorias_b > 4) or (num_victorias_b == 6 and num_victorias_a > 4):
         return "Aun no termina"
    else:
         return "Invalido"
    return ""

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
