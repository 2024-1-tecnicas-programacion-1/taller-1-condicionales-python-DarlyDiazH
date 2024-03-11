def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    

    if divisor ==0:
        return "No existe division\n" \
                "Cociente: no existe\n" \
                "Residuo: no existe"
    
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    respuesta = ""

    if residuo == 0:
        respuesta = "La división es exacta. \n" 
    else:
        respuesta = "La división no es exacta. \n" 
            
    respuesta += "Cociente: " + str(cociente) + "\n"
    respuesta += "Residuo: " + str(residuo)

    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
