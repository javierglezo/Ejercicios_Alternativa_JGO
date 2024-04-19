def calcular_descuento(cantidad_componentes, cliente):
    if 10000 <= cantidad_componentes <= 20000:
        descuento = 0.10
    elif 20001 <= cantidad_componentes <= 40000:
        descuento = 0.15
    elif cantidad_componentes > 40000:
        descuento = 0.20
    else:
        descuento = 0
    
    # Reducción del descuento para el cliente COMMAQ
    if cliente == "COMMAQ":
        descuento -= 0.02
    
    # Descuento mejorado para el cliente BEL
    if cliente == "BEL":
        descuento += 0.01
    
    return descuento

def mostrar_menu():
    print("1. Calcular descuento")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad_componentes = int(input("Ingrese la cantidad de procesadores pedidos: "))
            cliente = input("Ingrese el nombre de su empresa (COMMAQ, BEL u otro): ").upper()
            
            descuento = calcular_descuento(cantidad_componentes, cliente)
            
            # Mostrar el descuento aplicado
            print(f"El descuento aplicado es del {descuento}".format)
        elif opcion == "2":
            print("Adios")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()

