def calcular_descuento(importe):
    if 100 <= importe <= 500:
        descuento = importe * 0.05  # Descuento del 5 % para importes entre 100 y 500 €
    elif importe > 500:
        descuento = importe * 0.08  # Descuento del 8 % para importes superiores a 500 €
    else:
        print("Lamentablemente no hay descuento disponible")
        return None
    return descuento

def calcular_diferencia(importe, descuento):
    diferencia = importe - descuento
    return diferencia

def mostrar_menu():
    print("1. Calcular descuento")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            importe_compra = float(input("Ingrese el importe de la compra: "))
            descuento = calcular_descuento(importe_compra)
            if descuento is not None:
                print("El importe del descuento es:", descuento, "€")
                diferencia = calcular_diferencia(importe_compra, descuento)
                print("La diferencia del importe tras el descuento es:", diferencia, "€")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
