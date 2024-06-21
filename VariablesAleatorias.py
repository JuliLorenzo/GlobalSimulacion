import random

def metodoaceptacionrechazo():
    print("Se utilizara G(x)=1")

    # Validar el valor de a y b
    while True:
        a = float(input("Ingresa el valor del extremo a: "))
        b = float(input("Ingresa el valor del extremo b: "))
        if b <= a:
            print("Error: el valor de b debe ser mayor que el valor de a. Por favor, inténtelo de nuevo.")
        else:
            break

    # Validar el valor de la pendiente
    while True:
        pendiente = float(input("Ingresa la pendiente de la funcion densidad: "))
        if pendiente == 0:
            print("Error: la pendiente debe ser distinta de 0. Por favor, inténtelo de nuevo.")
        else:
            break

    # Mostrar los valores ingresados
    print("\nValores ingresados:")
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"Funcion Densidad = {pendiente} * x")

    numerosaleatoriosr1 = []
    numerosaleatoriosr2 = []
    cantnumerosaleatorios = int(input("Ingrese la cantidad de r1 y r2 a probar: "))

    for _ in range(cantnumerosaleatorios):
        numeroaleatorio = random.uniform(0, 1)  # Generar aleatorio en el rango [0, 1]
        numerosaleatoriosr1.append(numeroaleatorio)

    for _ in range(cantnumerosaleatorios):
        numeroaleatorio = random.uniform(0, 1)  # Generar aleatorio en el rango [0, 1]
        numerosaleatoriosr2.append(numeroaleatorio)

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

    valoresaleatoriosx = []
    for num_aleatorio in numerosaleatoriosr1:
        vax = a + (b - a) * num_aleatorio
        valoresaleatoriosx.append(vax)

    listafx = []
    for vax in valoresaleatoriosx:
        fx = pendiente * vax
        listafx.append(fx)

    efesobreM = []
    for fx in listafx:
        fxsobrem = fx / M
        efesobreM.append(fxsobrem)

    # Implementación del método de aceptación-rechazo con mensajes
    aceptaciones = 0
    print("\nResultados de aceptación-rechazo:")
    for i in range(cantnumerosaleatorios):
        if listafx[i] > numerosaleatoriosr2[i]:
            aceptaciones += 1
            print(f"r1: {numerosaleatoriosr1[i]:.2f}, r2: {numerosaleatoriosr2[i]:.2f} -> Aceptado")
        else:
            print(f"r1: {numerosaleatoriosr1[i]:.2f}, r2: {numerosaleatoriosr2[i]:.2f} -> Rechazado")

    # Mostrar resultados
    print(f"\nNúmero total de aceptaciones: {aceptaciones}")
    print(f"\nNúmero total de rechazos: {cantnumerosaleatorios - aceptaciones}")

## Metodo transformada inversa discreta
def transformada_inversa_discreta():
    num_intervalos = 0
    while num_intervalos <= 0:
        num_intervalos = int(input("Ingrese la cantidad de intervalos (debe ser mayor a 0): "))
        if num_intervalos <= 0:
            print("Error: El número de intervalos debe ser mayor a 0.")

    frecuencia_relativa = []
    suma_frecuencia_relativa = 0

    print("\nPor favor, ingrese la frecuencia relativa para cada intervalo:")
    while suma_frecuencia_relativa != 1.0:
        frecuencia_relativa = []
        suma_frecuencia_relativa = 0
        for i in range(num_intervalos):
            frec_rel = float(input(f"Intervalo {i+1}: "))
            frecuencia_relativa.append(frec_rel)
            suma_frecuencia_relativa += frec_rel

        if suma_frecuencia_relativa != 1.0:
            print("Error: La suma de las frecuencias relativas debe ser igual a 1.0. Por favor, ingrese nuevamente las frecuencias relativas.")

    frecuencia_absoluta = [round(sum(frecuencia_relativa[:i+1]) * 100, 2) for i in range(num_intervalos)]

    print("\nTabla de valores:")
    print("Intervalo | Frecuencia relativa | Frecuencia absoluta")
    for i in range(num_intervalos):
        print(f"  {i+1}\t|\t   {frecuencia_relativa[i]}\t|\t   {frecuencia_absoluta[i]/100}")

    variables_aleatorias = [round(random.random(), 3) for _ in range(10)]
    variables_aleatorias.sort()

    print("\nTabla de variables aleatorias generadas:")
    print("n\t|\t   u\t|\t   Valor")
    for i, u in enumerate(variables_aleatorias):
        for j, freq_abs in enumerate(frecuencia_absoluta):
            if u * 100 <= freq_abs:
                print(f"  {i+1}\t|\t   {u}\t|\t   {j+1}")
                break

    conteo_intervalos = [0] * num_intervalos
    for u in variables_aleatorias:
        for j, freq_abs in enumerate(frecuencia_absoluta):
            if u * 100 <= freq_abs:
                conteo_intervalos[j] += 1
                break

    print("\nValores de variables aleatorias por intervalos:")
    for i, conteo in enumerate(conteo_intervalos):
        print(f"Intervalo {i+1}: {conteo}")








