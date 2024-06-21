import statistics
import scipy.stats as stats
from scipy.stats import kstwobign
import random
import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox


#PRUEBA KOLMOGOROV SMIRNOV
def generacionNumeros():
    sucesion = []
    print("Como desea obtener la sucesion de numeros aleatorios? Seleccione una opcion:"
          "\n1. Ingresar los numeros aleatorios"
          "\n2. Generar los numeros de forma aleatoria")
    respuesta = int(input("\nOpcion seleccionada: "))

    print("\nIngrese la cantidad de numeros aleatorios: ", end="")
    cantidad = validarCantidadIngresada()

    if respuesta == 1:
        sucesion = validarSucesionNumAleatorios(cantidad)
    elif respuesta == 2:
        sucesion = generarSucesionAleatoria(cantidad)

    return sucesion

def generarSucesionAleatoria(cantidad):
    sucesion = [random.random() for i in range(cantidad)]
    return sucesion


def validarSucesionNumAleatorios(cantidad):
    sucesion=[]

    for i in range(cantidad):
        print("\tNumero Aleatorio", i + 1,":", end="")
        numeroAleatorio = validarNumeroAleatorio()
        sucesion.append(numeroAleatorio)

    return sucesion

def validarNumeroAleatorio():
    while True:
        numeroAleatorio = float(input())
        if 0 <= numeroAleatorio <= 1:
            return numeroAleatorio
        else:
            print("Error. El numero aleatorio debe tomar valores entre 0 y 1. Reeingrese el valor: ", end="")

def valorCriticoKS(n, nivelSignificancia):
    return stats.ksone.ppf(1 - nivelSignificancia, n)
    #return kstwobign.ppf(1 - nivelSignificancia) / np.sqrt(n)

def KolmogorovSmirnov(sucesion):
    if (sucesion == 1):
        numerosAleatorios = generacionNumeros()
    else:
        numerosAleatorios = sucesion

    nivelSignificancia = validarNivelSignificancia()

    numerosAleatorios.sort()
    i = 1
    n = len(numerosAleatorios)
    diferenciaMax = 0

    for num in numerosAleatorios:
        diferencia = abs(num - (i/n))
        if diferencia > diferenciaMax:
            diferenciaMax = diferencia
        i += 1

    valorCritico = valorCriticoKS(n, nivelSignificancia)

    #Criterio de aceptación
    if diferenciaMax < valorCritico:
        print("\nLa hipotesis se acepta. El estadístico calculado es igual a", diferenciaMax," < que el estadístico de la tabla:", valorCritico)

    else:
        print("\nLa hipotesis se rechaza. El estadístico calculado es igual a", diferenciaMax," > que el estadístico de la tabla:", valorCritico)


#PRUEBA CHI CUADRADA

def validarIntervalo():
    while True:
        k = int(input("Ingrese la cantidad de intervalos: "))
        if (k > 0):
            return k
        else:
            print("Error. Ingrese un numero de intervalos mayor a cero")

def generar_sucesion(k):
    sucesion=[]
    print("\nIngrese la cantidad de números observados en cada intervalo:")

    for i in range(k):
        print("\tIntervalo", i + 1,":")
        cantidad = validarCantidadIngresada()
        sucesion.append(cantidad)

    return sucesion

def validarCantidadIngresada():
      while True:
          cantidad = int(input("\tCantidad: "))
          if (cantidad > 0):
            return cantidad
          else:
            print("Error. Ingrese un valor mayor a cero")

def validarNivelSignificancia():
    while True:
        nivelSignificancia = float(input("Ingrese el valor de Nivel de significancia: "))
        if (0 < nivelSignificancia < 1 ):
            return nivelSignificancia
        else:
            print("Error. Ingrese un valor de Nivel de significancia mayor a 0 y menor a 1")

def valorCriticoChi2(gradosLibertad, nivelSignificancia):
    return stats.chi2.ppf(1 - nivelSignificancia, gradosLibertad)

def PruebaChi2():
      k = validarIntervalo()
      gradosLibertad = k - 1
      nivelSignificancia = validarNivelSignificancia()
      sucesion = generar_sucesion(k)

      valorCritico = round(valorCriticoChi2(gradosLibertad, nivelSignificancia), 3)
      chi2_suma = 0

      # Calcula la frecuencia esperada a partir de la sucesion de números observados
      frec_esperada= statistics.mean(sucesion)
      print("\nLa frecuencia esperada es:", frec_esperada)

      #Calcula el valor chi cuadrada
      for elemento in sucesion:
          chi2_suma = round(chi2_suma + (((elemento - frec_esperada)**2)/frec_esperada), 3)

      #Criterio de aceptación
      if chi2_suma < valorCritico:
          print("\nLa hipotesis se acepta. El estadístico calculado es igual a", chi2_suma," < que el estadístico de la tabla:", valorCritico)

      else:
          print("\nLa hipotesis se rechaza. El estadístico calculado es igual a", chi2_suma," > que el estadístico de la tabla:", valorCritico)


#VALIDACIONES -> PENDIENTE

def validar_kolmogorov(numerosaleatorios):
    print(numerosaleatorios)
    estadistico = float(input("Ingrese el valor estadístico de la tabla Kolmogorov: "))

    maximadiferencia = KolmogorovSmirnov(numerosaleatorios)

    if maximadiferencia < estadistico:
        print(f"El generador de números aleatorios pasa la prueba K-S con el estadístico: {estadistico} y la diferencia máxima calculada de: {maximadiferencia}")
        print(f"{maximadiferencia} < {estadistico}")
    else:
        print(f"El generador de números aleatorios NO pasa la prueba K-S con el estadístico: {estadistico} y la diferencia máxima calculada de: {maximadiferencia}")
        print(f"{maximadiferencia} > {estadistico}")


def validar_ljung_box():
    """
    Valida una secuencia de números aleatorios utilizando la Prueba de Ljung-Box.

    :param numeros_aleatorios: Lista de números aleatorios generados.
    :param lags: Lista de lags para la prueba de Ljung-Box.
    :return: DataFrame con los resultados de la prueba de Ljung-Box.
    """
    laggs = int(input("Ingrese la cantidad de lags para la prueba "))
    lags = [laggs]
    numerosaleatorios = []
    cantnumerosaleatorios = int(input("Ingrese la cantidad de numeros aleatorios "))

    for _ in range(cantnumerosaleatorios):
        numeroaleatorio = random.uniform(0, 1)  # Generar aleatorio en el rango [0, 1]
        numerosaleatorios.append(numeroaleatorio)

    ljung_box_test = acorr_ljungbox(numerosaleatorios, lags=lags, return_df=True)
    print("Resultados de la prueba de Ljung-Box:")
    print(ljung_box_test)
    return ljung_box_test

def validar_aleatoriedad(numeros):
    while True:
        print("\nSeleccione la prueba estadística para validar la aleatoriedad:")
        print("1. Prueba de Chi Cuadrada")
        print("2. Prueba de Kolmogorov-Smirnov")
        print("3. Volver al menú principal")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            #validar_chi_cuadrada(numeros)
            break
        elif choice == '2':
            validar_kolmogorov(numeros)
            break
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
