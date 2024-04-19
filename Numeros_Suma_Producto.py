# Definición de la función para clasificar los números
def clasificar_numeros():
    # Solicitar al usuario que ingrese dos números y convertirlos a flotantes
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    # Calcular la suma y el producto de los números ingresados
    suma = a + b
    producto = a * b

    # Ordenar los números (producto, primer número, suma, segundo número) de menor a mayor
    numeros_ordenados = sorted([producto, a, suma, b])
    return numeros_ordenados  # Devolver la lista ordenada de números

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("1. Clasificar numeros")
    print("2. Salir")

# Función principal que controla la ejecución del programa
def main():
    while True:  # Bucle principal que se ejecuta hasta que el usuario elija salir
        mostrar_menu()  # Mostrar el menú de opciones
        opcion = input("Elige una opcion: ")  # Solicitar al usuario que elija una opción

        if opcion == "1":  # Si elige la opción 1, clasificar los números
            resultado = clasificar_numeros()  # Llamar a la función para clasificar los números
            print("Los números ordenados de menor a mayor son:", resultado)  # Imprimir los números ordenados
        elif opcion == "2":  # Si elige la opción 2, salir del programa
            print("Saliendo del programa...")
            break  # Salir del bucle y finalizar la ejecución
        else:  # Si elige una opción no válida, mostrar un mensaje de error
            print("Opcion no válida. Por favor, elige una opcion válida.")


if __name__ == "__main__":
    main()  
