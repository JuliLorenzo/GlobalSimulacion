import Generadores
import Validaciones
import VariablesAleatorias


def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Generacion de Numeros Aleatorios")
        print("2. Validacion de la Aleatoriedad de la Sucesion")
        print("3. Extraccion de Variables Aleatorias")
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
        print("\nSubmenú 1: Generacion de Numeros Aleatorios")

        print("1. Generar Numeros Aleatorios mediante el Método Congruencial Lineal Mixto")
        print("2. Generar Numeros Aleatorios mediante el Método Congruencial Lineal Multiplicativo")
        print("3. Generar Numeros Aleatorios mediante el Método del Cuadrado Medio")
        print("4. Comparar la Longitud de Periodo alcanzada por 2 Generadores")
        print("5. Volver al menú principal")

        choice = input("\nSeleccione una opcion: ")

        if choice == '1':
            print("\nGenerar Numeros Aleatorios mediante el Método Congruencial Lineal Mixto")
            numeros = Generadores.MetodoConguencialMixto()
            #preguntar_validar(numeros)
        elif choice == '2':
            print("\nGenerar Numeros Aleatorios mediante el Método Congruencial Lineal Multiplicativo")
            numeros = Generadores.MetodoCongruencialMultiplicativo()
            #preguntar_validar(numeros)
        elif choice == '3':
            print("\nGenerar Numeros Aleatorios mediante el Método del Cuadrado Medio")
            numeros = Generadores.MetodoDelCuadradoMedio()
            #preguntar_validar(numeros)
        elif choice == '4':
            print("\nComparar la Longitud de Periodo de 2 Generadores")
            Generadores.compararGeneradores()
        elif choice == '5':
            return
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

        if volverMenuPrincipal():
            break
        else:
            exit("Hasta luego!")

def submenu_2():
    while True:
        print("\nSubmenú 2: Pruebas estadisticas para validar la aleatoriedad de la sucesion")
        print("1. Prueba de la Chi Cuadrada")
        print("2. Prueba de Kolmogorov Smirnov")
        print("3. Prueba o Test de rachas")
        print("4. Test de autocorrelacion Ljung-Box")
        print("5. Volver al menú principal")

        choice = input("\nSelecciona una Prueba Estadistica: ")

        if choice == '1':
            print("\nPrueba de la Chi Cuadrada")
            Validaciones.PruebaChi2()
        elif choice == '2':
            print("\nPrueba de Kolmogorov Smirnov")
            Validaciones.KolmogorovSmirnov(1)
        elif choice == '3':
            print("\nPrueba o Test de rachas")
            # Implement validation logic for Prueba Serial

        elif choice == '4':
            print("\nPrueba de autocorrelacion Ljung-Box")
            Validaciones.validar_ljung_box()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

        if volverMenuPrincipal():
            break
        else:
            exit("Hasta luego!")

def submenu_3():
    while True:
        print("\nSubmenú 3: Extraer Variables Aleatorias")
        print("1. Transformada Inversa Caso Discreto")
        print("2. Metodo de Aceptacion Rechazo")
        print("3. Volver al menú principal")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            print("Transformada Inversa Caso Discreto")
            VariablesAleatorias.transformada_inversa_discreta()
        elif choice == '2':
            print("Metodo de Aceptacion Rechazo")
            VariablesAleatorias.metodoaceptacionrechazo()
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
def preguntar_validar(numeros):
    while True:
        respuesta = input("\n¿Desea validar la aleatoriedad de los números generados? Ingrese SI o NO: ").strip().upper()
        if respuesta == "SI":
            Validaciones.validar_aleatoriedad(numeros)
            break
        elif respuesta == "NO":
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def volverMenuPrincipal():
    while True:
        respuesta = input("\n¿Desea volver al menú principal?\nIngrese SI o NO: ").strip().upper()
        if respuesta == "SI":
            return True
        elif respuesta == "NO":
            return False
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
