import Generadores

def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Generar Numeros Aleatorios")
        print("2. Validar Aleatoriedad de la Sucesion")
        print("3. Generar variables aleatorias")
        print("4. Salir")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            submenu_1()
        elif choice == '2':
            submenu_2()
        elif choice == '3':
            submenu_3()
        elif choice == '4':
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def submenu_1():
    while True:
        print("\nSubmenú 1: Metodos de Generacion de Numeros Aleatorios")

        print("1. Método Congruencial Lineal Mixto")
        print("2. Método Congruencial Lineal Multiplicativo")
        print("3. Método del Cuadrado Medio")
        #print("4. Comparar Generadores")
        print("4. Volver al menú principal")

        choice = input("\nSeleccione el Metodo a utilizar: ")

        if choice == '1':
            print("\nMétodo Congruencial Lineal Mixto")
            Generadores.MetodoConguencialLineal()
            break
        elif choice == '2':
            print("\nMétodo Congruencial Lineal Multiplicativo")
            Generadores.MetodoCongruencialMultiplicativo()
        elif choice == '3':
            print("\nMétodo del Cuadrado Medio")
            Generadores.MetodoDelCuadradoMedio()
        elif choice == '4':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def submenu_2():
    while True:
        print("\nSubmenú 2: Pruebas estadisticas para validar la aleatoriedad de la sucesion")
        print("1. Prueba de la Chi Cuadrada")
        print("2. Prueba de Kolmogorov Smirnov")
        print("3. Prueba Serial")
        print("4. Prueba o Test de rachas")
        print("5. Prueba de Poker")
        print("6. Volver al menú principal")

        choice = input("\nSelecciona una Prueba Estadistica: ")

        if choice == '1':
            print("\nPrueba de la Chi Cuadrada")
        elif choice == '2':
            print("\nPrueba de Kolmogorov Smirnov")
        elif choice == '3':
            print("\nPrueba Serial")
        elif choice == '4':
            print("\nPrueba o Test de rachas")
        elif choice == '5':
            print("\nVolver al menú principal")
        elif choice == '6':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def submenu_3():
    while True:
        print("\nSubmenú 3: Generar Variables Aleatorias")
        print("1. Subopción 3.1")
        print("2. Subopción 3.2")
        print("3. Volver al menú principal")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            print("1. ")
        elif choice == '2':
            print("2. ")
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
