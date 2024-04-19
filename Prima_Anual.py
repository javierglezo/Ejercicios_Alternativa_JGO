def calcular_prima_por_accidentes(accidentes):
    if accidentes == 0:
        return 1.0  
    elif accidentes == 1:
        return 1/2  
    elif accidentes == 2:
        return 1/3  
    elif accidentes == 3:
        return 1/4  
    else:
        return 0.0  

def calcular_prima_distancia(kilometros):
    prima_distancia = min(400, 0.01 * kilometros)
    return prima_distancia

def calcular_prima_antiguedad(years_servicio):
    if years_servicio >= 4:
        return 200 + 20 * (years_servicio - 4)
    else:
        return 0

def calcular_prima_anual(accidentes, responsabilidad, kilometros, antiguedad):
    prima_accidentes = calcular_prima_por_accidentes(accidentes)
    prima_distancia = calcular_prima_distancia(kilometros)
    prima_antiguedad = calcular_prima_antiguedad(antiguedad)

    prima_total = prima_distancia + prima_antiguedad 

    if responsabilidad > 20:
        prima_total *= prima_accidentes

    return prima_total

def main():
    accidentes = int(input("Ingrese el número de accidentes del conductor: "))
    responsabilidad = float(input("Ingrese el porcentaje de responsabilidad del conductor: "))
    kilometros = float(input("Ingrese la cantidad de kilómetros recorridos durante el año: "))
    antiguedad = int(input("Ingrese los años de antigüedad del conductor: "))

    prima_total = calcular_prima_anual(accidentes, responsabilidad, kilometros, antiguedad)
    print("El dinero total ganado de prima es: {} €".format(prima_total))

if __name__ == "__main__":
    main()
