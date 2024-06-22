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
            numeros = Generadores.MetodoConguencialMixto()
            preguntar_validar(numeros)
        elif choice == '2':
            numeros = Generadores.MetodoCongruencialMultiplicativo()
            preguntar_validar(numeros)
        elif choice == '3':
            numeros = Generadores.MetodoDelCuadradoMedio()
            preguntar_validar(numeros)
        elif choice == '4':
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
            Validaciones.PruebaChi2()
        elif choice == '2':
            Validaciones.KolmogorovSmirnov()
        elif choice == '3':
            Validaciones.TestDeRachas()
        elif choice == '4':
            Validaciones.LjungBox()
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
            VariablesAleatorias.transformada_inversa_discreta()
        elif choice == '2':
            VariablesAleatorias.metodoaceptacionrechazo()
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

        if volverMenuPrincipal():
            break
        else:
            exit("Hasta luego!")

def preguntar_validar(numeros):
    while True:
        respuesta = input("\n¿Desea validar la aleatoriedad del Generador? Ingrese SI o NO: ").strip().upper()
        if respuesta == "SI":
            opcionesValidacion(numeros)
            break
        elif respuesta == "NO":
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def opcionesValidacion(numeros):
    print("\nValidaciones disponibles:"
      "\n1. Evaluar la uniformidad de los números aleatorios mediante la Prueba de Kolmogorov Smirnov "
      "\n2. Evaluar la independencia de los números aleatorios mediante el Test de Rachas"
      "\n3. Realizar ambas validaciones")

    while True:
        respuesta = int(input("\nIngrese una opcion: "))
        if respuesta == 1:
            Validaciones.KolmogorovSmirnov(numeros)
            break
        if respuesta == 2:
            Validaciones.TestDeRachas(numeros)
            break
        elif respuesta == 3:
            Validaciones.KolmogorovSmirnov(numeros)
            input("\nIngrese enter para continuar con la validacion de independencia de los números aleatorios mediante el Test de Rachas\n")
            Validaciones.TestDeRachas(numeros)
            break
        else:
            print("Error. Ingrese una opcion valida")

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
