def calcular_descuento(importe, num_niños):
    if num_niños == 2:
        descuento = importe * 0.10
    elif num_niños == 3:
        descuento = importe * 0.15
    elif num_niños == 4:
        descuento = importe * 0.18
    elif num_niños > 4:
        descuento = importe * 0.18 + (num_niños - 4) * 0.01
    else:
        descuento = 0  # No se aplica descuento si no hay niños

    return descuento

def mostrar_menu():
    print("1. Calcular descuento")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            importe = float(input("Ingrese el importe de la entrada al Parque Warner Madrid: "))
            num_niños = int(input("Ingrese el número de niños en la familia: "))
            
            descuento = calcular_descuento(importe, num_niños)
            nuevo_importe = importe - descuento
            
            print(f"El descuento aplicado es: {descuento} €")
            print(f"El importe con el descuento aplicado es: {nuevo_importe} €")
        elif opcion == "2":
            print("Gracias")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
