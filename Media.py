# Definición de la función para calcular la media de las notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Definición de la función para evaluar al alumno según su media
def ranking_alumno(media):
    if media > 15:
        evaluacion = "Alumno con talento"
    elif 12 <= media <= 15:
        evaluacion = "Con capacidad"
    else:
        evaluacion = "Debe reorientarse"
    return evaluacion

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("1. Calcular media y evaluación")
    print("2. Salir")

# Función principal del programa
def main():
    while True:  # Bucle que se ejecuta hasta que el usuario elija salir
        mostrar_menu()  # Mostrar el menú de opciones
        opcion = input("Elige una opción: ")  # Solicitar al usuario que elija una opción

        if opcion == "1":  # Si elige la opción 1, calcular la media y la evaluación
            # Solicitar al usuario que ingrese las cuatro notas
            notas = []
            for i in range(4):
                nota = float(input(f"Ingrese la nota {i+1}: "))
                notas.append(nota)

            # Calcular la media de las notas
            media = calcular_media(notas)

            # Evaluar al alumno según su media
            evaluacion = ranking_alumno(media)

            # Mostrar la media y la evaluación
            print("La media de las notas es: ", media)
            print("Evaluación:", evaluacion)
        elif opcion == "2":  # Si elige la opción 2, salir del programa
            print("Saliendo del programa...")
            break
        else:  # Si elige una opción no válida, mostrar un mensaje de error
            print("Opción no válida. Por favor, elige una opción válida.")

# Verificar si este archivo es el programa principal que se está ejecutando
if __name__ == "__main__":
    main()  # Llamar a la función principal para iniciar el programa
