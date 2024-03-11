from time import localtime


def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    t = localtime()
    currentDia = t.tm_mday
    currentMes = t.tm_mon
    currentAnno = t.tm_year
    
    edad = currentAnno - anno
    if mes > currentMes or (mes == currentMes and dia > currentDia):
        edad -= 1

    return "Usted tiene {} años".format(edad)

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
