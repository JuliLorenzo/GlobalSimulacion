import math
import statistics
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import kstwobign
import random
import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox
from tabulate import tabulate
import pandas as pd

#PRUEBA DE RACHAS

def contarRachas(sucesion):
    media = 0.5
    N = len(sucesion)
    n1 = sum(1 for num in sucesion if num >= media)
    n2 = N - n1

    rachas = 0
    racha_actual = None

    for num in sucesion:
        if num >= media:
            if racha_actual != '+':
                rachas += 1
                racha_actual = '+'
        else:
            if racha_actual != '-':
                rachas += 1
                racha_actual = '-'

    return n1, n2, N, rachas

def calcularZ0(n1, n2, N, rachas):
    u = (2 * n1 * n2) / N + 1/2
    o = math.sqrt(((2 * n1 * n2) * (2 * n1 * n2 - N)) / (N**2 * (N - 1)))
    z0 = (rachas - u) / o
    return z0

def tipoComparacion():
    print("Para determinar el valor critico Z, desea ingresar: \n1. Nivel de Significancia \n2. Valor Critico Z")
    while True:
        respuesta = int(input("\nIngrese una opcion: "))
        if respuesta == 1:
            nivelSignificancia = validarNivelSignificancia()
            return norm.ppf(1 - nivelSignificancia / 2)
        elif respuesta == 2:
            valorCritico = float(input("Ingrese el valor del estadistico Z: "))
            return abs(valorCritico)
        else:
            print("\nError. Las opciones validas son: 1 y 2")


def TestDeRachas(sucesion=None):
    print("\nPrueba o Test de rachas")
    if sucesion is None:
        numerosAleatorios = generacionNumeros()
    else:
        numerosAleatorios = sucesion

    n1, n2, N, rachas = contarRachas(numerosAleatorios)
    estadisticoZ0 = round(calcularZ0(n1, n2, N, rachas), 3)
    valorCritico = round(tipoComparacion(), 4)

    tabla = [
    ["n1 (+)", n1],
    ["n2 (-)", n2],
    ["N", N],
    ["Rachas", rachas],
    ["Z0", estadisticoZ0],
    ["Valor Crítico", f"±{valorCritico}"]
    ]

    print(tabulate(tabla, headers=["Variable", "Valor"], tablefmt="grid"))

    if -valorCritico < estadisticoZ0 < valorCritico:
        print("\nEl estadístico calculado se encuentra entre los valores cirticos de z:", -valorCritico,"<=",estadisticoZ0,"<=",valorCritico)
        print("No hay evidencia suficiente para rechazar la hipotesis nula. Lo que sugiere que los números aleatorios son independientes.")

    else:
        print("\nEl estadistico", estadisticoZ0, "cae fuera del rango")
        print("Se rechaza la hipótesis nula. Lo que sugiere que la secuencia de números no son independientes")



#PRUEBA KOLMOGOROV SMIRNOV
def generacionNumeros():
    while True:
        print("Como desea obtener la sucesion de numeros aleatorios? Seleccione una opcion:"
              "\n1. Ingresar los numeros aleatorios"
              "\n2. Generar los numeros de forma aleatoria")
        respuesta = int(input("\nOpcion seleccionada: "))

        print("\nIngrese la cantidad de numeros aleatorios")
        cantidad = validarCantidadIngresada()

        if respuesta == 1:
            return validarSucesionNumAleatorios(cantidad)
        elif respuesta == 2:
            return generarSucesionAleatoria(cantidad)
        else:
            print("Error. Ingrese una opcion valida")


def generarSucesionAleatoria(cantidad):
    sucesion = []
    datosTabla = []
    for i in range(cantidad):
        x = round(random.random(), 3)
        datosTabla.append((i+1, x))
        sucesion.append(x)

    print("\nNumeros Aleatorios generados:")
    print(tabulate(datosTabla, headers=["i", "Numero Aleatorio u"], tablefmt="grid", colalign=("center", "center")))
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

def KolmogorovSmirnov(sucesion=None):
    print("\nPrueba de Kolmogorov Smirnov")

    if sucesion is None:
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

    valorCritico = round(valorCriticoKS(n, nivelSignificancia), 3)


    if diferenciaMax < valorCritico:
        print("\nEl estadístico calculado es igual a", diferenciaMax," < que el estadístico de la tabla:", valorCritico)
        print("No hay evidencia suficiente para rechazar la hipotesis nula. Lo que sugiere que la secuencia de números aleatorios sigue la distribución uniforme.")

    else:
        print("\nEl estadístico calculado es igual a", diferenciaMax," > que el estadístico de la tabla:", valorCritico)
        print("Se rechaza la hipótesis nula. Lo que sugiere que la secuencia de números no sigue la distribución uniforme")


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
          cantidad = int(input("Cantidad: "))
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
    print("\nPrueba de la Chi Cuadrada")
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
        print("\nEl estadístico calculado es igual a", chi2_suma," < que el estadístico de la tabla:", valorCritico)
        print("No hay evidencia suficiente para rechazar la hipotesis nula. Lo que sugiere que la secuencia de números aleatorios sigue la distribución uniforme.")

    else:
        print("\El estadístico calculado es igual a", chi2_suma," > que el estadístico de la tabla:", valorCritico)
        print("Se rechaza la hipótesis nula. Lo que sugiere que la secuencia de números no sigue la distribución uniforme")

def validarCantidadLags(cantNumeros):
    while True:
        lags = int(input("\nIngrese la cantidad de lags: "))
        if 0 < lags < cantNumeros:
            return lags
        else:
            print("Error. La cantidad de lags debe ser mayor a 0 y menor o igual a",cantNumeros,"(cantidad de numeros aleatorios)")

def imprimirResultados(Qestadistico, valorCritico, pValor):
    print("\nResultados de la prueba de Ljung-Box:")
    print("-" * 47)  # Línea horizontal de separación
    print(f"| {'Métrica':^30} | {'Valor':^12} |")
    print("-" * 47)  # Línea horizontal de separación
    print(f"| {'Estadístico Q':^30} | {Qestadistico:.3f} |")
    print(f"| {'Valor crítico chi-cuadrado':^30} | {valorCritico:.3f} |")
    print(f"| {'P-valor':^30} | {pValor:.3f} |")
    print("-" * 47)  # Línea horizontal de separación

def LjungBox():
    print("\nPrueba de Autocorrelacion Ljung-Box")
    numerosAleatorios = generacionNumeros()
    cantNumeros = len(numerosAleatorios)

    lags = validarCantidadLags(cantNumeros)
    nivelSignificancia = validarNivelSignificancia()

    resultado = acorr_ljungbox(numerosAleatorios, lags=lags)

    if isinstance(resultado, pd.DataFrame):
        resultado = resultado.iloc[-1]

    Qestadistico = round(resultado['lb_stat'], 3)
    pValor = round(resultado['lb_pvalue'], 3)
    gradosLibertad = lags

    valorCritico = round(valorCriticoChi2(gradosLibertad, nivelSignificancia), 3)

    imprimirResultados(Qestadistico, valorCritico, pValor)

    if Qestadistico < valorCritico:
        print("\nEl estadístico calculado es igual a", Qestadistico,"< que el estadístico de la tabla:", valorCritico)
        print("Por lo tanto, no hay evidencia suficiente para rechazar la hipotesis nula de no autocorrelacion")

    else:
        print("\nEl estadístico calculado es igual a", Qestadistico," > que el estadístico de la tabla:", valorCritico)
        print("Se rechaza la hipótesis nula. Lo que sugiere que la secuencia de números aleatorios presenta una autocorrelacion significativa")

    confianza = round((1 - nivelSignificancia) * 100, 3)

    print("\nInterpretacion p-valor:")
    if pValor > nivelSignificancia:
        print("El p-valor obtenido es igual a", pValor, "> que el Nivel de Significancia elegido α =",nivelSignificancia)
        print("Esto implica que no se rechaza la hipótesis nula con un",confianza,"% de confianza.")
    else:
        print("El p-valor obtenido es igual a", pValor, "< que el Nivel de Significancia elegido α =",nivelSignificancia)
        print("Esto implica que se rechaza la hipótesis nula con un",confianza,"% de confianza.")


