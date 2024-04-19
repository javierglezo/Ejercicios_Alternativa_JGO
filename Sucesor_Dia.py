from enum import Enum

# Definición del enumerado para los días de la semana
class Dia(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5
    DOMINGO = 6

# Función para obtener el día siguiente
def sucesor(dia):
    dia = (dia.value + 1) % 7  # Calcula el valor del día siguiente dentro del rango 0-6
    return Dia(dia)  # Retorna el día siguiente como un objeto del tipo Dia

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("1. Obtener el día siguiente")
    print("2. Salir")

# Función principal del programa
def main():
    while True:
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Elige una opción: ")  # Solicita al usuario que elija una opción

        if opcion == "1":
            entrada_inicio = input("Escribe el día de la semana actual: ")  # Solicita al usuario que ingrese el día actual
            dia_usuario = Dia[entrada_inicio.upper()]  # Convierte la entrada del usuario a un objeto Dia
            dia_siguiente_usuario = sucesor(dia_usuario)  # Calcula el día siguiente
            print("El día siguiente a", dia_usuario.name, "es", dia_siguiente_usuario.name)  # Muestra el resultado
        elif opcion == "2":
            print("Fin del programa")  # Mensaje de despedida
            break  # Sale del bucle while y termina el programa
        else:
            print("Opción no válida. Por favor, elige una opción válida.")  # Mensaje de error si la opción no es válida

if __name__ == "__main__":
    main()
