

from tabulate import tabulate

import Validaciones

def validarIntervaloAB():
    a = float(input("\nIngresa el valor del extremo inferior a: "))
    while True:
        b = float(input("Ingresa el valor del extremo superior b: "))
        if b <= a:
            print("ERROR: el valor de b debe ser mayor que el valor de a. Ingrese un nuevo valor para b:", end="")
        else:
            break
    return a,b

def validarCantidadIgual(lista1, lista2):
    while len(lista1) != len(lista2):
        print("\nERROR: Ambas listas deben tener la misma cantidad de numeros aleatorios.")
        print("Por favor, vuelve a ingresar la segunda sucesion de Numeros Aleatorios r2.\n")
        lista2 = Validaciones.generacionNumeros()
    return lista2

def metodoaceptacionrechazo():
    print("\nMetodo de Aceptacion Rechazo")
    print("Se utilizara G(x)=1")

    a, b = validarIntervaloAB()

    # Validar el valor de la pendiente
    while True:
        pendiente = float(input("Ingresa la pendiente de la funcion densidad: "))
        if pendiente == 0:
            print("Error: la pendiente debe ser distinta de 0. Por favor, inténtelo de nuevo.")
        else:
            break

    # Mostrar los valores ingresados
    valores_ingresados = [
        ["a", a],
        ["b", b],
        ["f(x)", f"{pendiente} * x"]
    ]
    print("\nValores ingresados:")
    print(tabulate(valores_ingresados, headers=["Variable", "Valor"], tablefmt="grid"))

    # Crear una lista de números entre a y b
    numeros = [a + i * (b - a) / 10 for i in range(11)]

    # Multiplicar cada número por la pendiente
    valores_multiplicados = [pendiente * x for x in numeros]

    # Encontrar el máximo de los valores obtenidos
    M = max(valores_multiplicados)

    # Imprimir los valores en forma de tabla
    print("\nFuncion Densidad:")
    print("=================")
    print("|   x   |   f(x)   |")
    print("=================")
    for x, valor in zip(numeros, valores_multiplicados):
        print(f"|  {x:.2f}  |  {valor:.2f}  |")
    print("=================")

    print("\nPrimera sucesion de Numeros Aleatorios r1")
    numerosaleatoriosr1 = Validaciones.generacionNumeros()
    print("\nSegunda sucesion de Numeros Aleatorios r2")
    numerosaleatoriosr2 = Validaciones.generacionNumeros()
    numerosaleatoriosr2 = validarCantidadIgual(numerosaleatoriosr1,numerosaleatoriosr2)

    valoresaleatoriosx = []
    for num_aleatorio in numerosaleatoriosr1:
        vax = a + (b - a) * num_aleatorio
        valoresaleatoriosx.append(vax)

    listafx = []
    for vax in valoresaleatoriosx:
        fx = pendiente * vax
        listafx.append(fx)

    fsobreM = []
    for fx in listafx:
        fxsobrem = fx / M
        fsobreM.append(fxsobrem)

    cantNumerosAleatorios = len(numerosaleatoriosr1)
    resultados = []

    for i in range(cantNumerosAleatorios):
        if fsobreM[i] >= numerosaleatoriosr2[i]:
            resultados.append("Aceptado")
        else:
            resultados.append("Rechazado")

    tabla = []
    for i in range(cantNumerosAleatorios):
        tabla.append([numerosaleatoriosr1[i], numerosaleatoriosr2[i], valoresaleatoriosx[i], listafx[i], fsobreM[i], resultados[i]])

    print("\nResultados de aceptación-rechazo:")
    print(tabulate(tabla, headers=["r1", "r2", "vax", "f(x)", "f(x)/M", "Resultado"], tablefmt="grid", colalign=("center", "center")))

    aceptaciones = resultados.count("Aceptado")
    print(f"\nNúmero total de aceptaciones: {aceptaciones}")
    print(f"Número total de rechazos: {cantNumerosAleatorios - aceptaciones}")


def validarIntervalo():
    while True:
        k = int(input("Ingrese la cantidad de intervalos: "))
        if (k > 0):
            return k
        else:
            print("Error. Ingrese un numero de intervalos mayor a cero")

def validarValor():
    while True:
      x = int(input())
      if (x >= 0):
        return x
      else:
        print("Error. Ingrese una cantidad mayor o igual a cero")

def validarFrecuenciaAbsoluta(k):
    print("\nIngrese la cantidad de observaciones (FA) de cada intervalo")
    fAbsolutaList = []
    sumaFA = 0

    for i in range(k):
        print("\tIntervalo", i + 1,":", end="")
        fAbsoluta = validarValor()
        fAbsolutaList.append(fAbsoluta)
        sumaFA += fAbsoluta

    return fAbsolutaList, sumaFA

def calculoFrecuenciaRelativa(FAbsolutas, Total):
    fRelativaList = []
    for i in FAbsolutas:
        fRelativa = i/Total
        fRelativaList.append(fRelativa)
    return fRelativaList

def imprimir_tabla_frecuencias(intervalos, frecuenciasRelativas, frecuenciasAcumuladas):
    print("\nTabla de valores de Frecuencias:")
    print("------------------------------------------------------------")
    print(f"|{' Intervalo ':^11}|{' Frecuencia Relativa ':^22}|{' Frecuencia Acumulada ':^23}|")
    print("------------------------------------------------------------")
    for i in range(intervalos):
        print(f"|{i + 1:^11}|{frecuenciasRelativas[i]:^22.3f}|{frecuenciasAcumuladas[i]:^23.3f}|")
    print("-------------------------------------------------------------")

def imprimir_tabla_numeros_aleatorios(numerosAleatorios, frecuenciasAcumuladas):
    print("\nTabla de extracción de la variable aleatoria:")
    print("-------------------------")
    print("|  i  |    u    |   x   |")
    print("-------------------------")
    for i, u in enumerate(numerosAleatorios):
        for j, fAcum in enumerate(frecuenciasAcumuladas):
            if u <= fAcum:
                x = j + 1
                print(f"| {i + 1:^3} | {u:^7.3f} | {x:^5} |")
                break
    print("-------------------------")

def imprimir_tabla_variables_aleatorias_por_intervalo(conteoIntervalos):
    print("\nValores de variables aleatorias por intervalos:")
    print("----------------------------")
    print(f"|{' Intervalo ':^11}|{' Conteo ':^10}|")
    print("----------------------------")
    for i, conteo in enumerate(conteoIntervalos):
        print(f"|{i + 1:^11}|{conteo:^10}|")
    print("----------------------------")

def imprimir_tabla_observaciones(fAbsolutaList):
    print("\nTabla de observaciones por intervalo:")
    print("------------------------------------")
    print(f"|{' Intervalo ':^11}|{' Frecuencia Absoluta ':^20}|")
    print("------------------------------------")
    for i, fAbsoluta in enumerate(fAbsolutaList):
        print(f"|{i + 1:^11}|{fAbsoluta:^20}|")
    print("------------------------------------")

## Metodo transformada inversa discreta
def transformada_inversa_discreta():
    print("\nTransformada Inversa Caso Discreto")
    intervalos = validarIntervalo()

    frecuenciasAbsolutas, totalObs = validarFrecuenciaAbsoluta(intervalos)
    frecuenciasRelativas = calculoFrecuenciaRelativa(frecuenciasAbsolutas, totalObs)

    imprimir_tabla_observaciones(frecuenciasAbsolutas)

    frecuenciasAcumuladas = [round(sum(frecuenciasRelativas[:i+1]), 3) for i in range(intervalos)]

    imprimir_tabla_frecuencias(intervalos, frecuenciasRelativas, frecuenciasAcumuladas)
    print()
    numerosAleatorios = Validaciones.generacionNumeros()

    imprimir_tabla_numeros_aleatorios(numerosAleatorios, frecuenciasAcumuladas)

    conteoIntervalos = [0] * intervalos
    for u in numerosAleatorios:
        for j, fAcum in enumerate(frecuenciasAcumuladas):
            if u <= fAcum:
                conteoIntervalos[j] += 1
                break

    imprimir_tabla_variables_aleatorias_por_intervalo(conteoIntervalos)










