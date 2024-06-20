# validaciones.py

def KolmogorovSmirnov(numerosaleatorios):
    cantnumerosaleatorios = len(numerosaleatorios)
    listaordenada = sorted(numerosaleatorios)
    numerosrestados = []
    contador = 1
    for i in listaordenada:
        FDA_Esperada = contador / cantnumerosaleatorios
        valorabsolutoresta = abs(i - FDA_Esperada)
        numerosrestados.append(valorabsolutoresta)
        contador += 1

    maximadiferencia = max(numerosrestados)
    return maximadiferencia

def chi_cuadrada(numerosaleatorios):
    cantnumerosaleatorios = len(numerosaleatorios)
    k = int(input("Ingrese el número de intervalos (k): "))
    frec_esperada = cantnumerosaleatorios / k
    intervalos = [0] * k

    for numero in numerosaleatorios:
        indice = int(numero * k)
        if indice == k:  # Corrección para el valor 1.0
            indice -= 1
        intervalos[indice] += 1

    chi_cuadrado = sum(((frec_observada - frec_esperada) ** 2) / frec_esperada for frec_observada in intervalos)
    return chi_cuadrado

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

def validar_chi_cuadrada(numerosaleatorios):
    print(numerosaleatorios)
    chi_critico = float(input("Ingrese el valor crítico de la tabla Chi-Cuadrada: "))

    chi_calculado = chi_cuadrada(numerosaleatorios)

    if chi_calculado < chi_critico:
        print(f"El generador de números aleatorios pasa la prueba de Chi-Cuadrada con el valor crítico: {chi_critico} y el valor calculado de: {chi_calculado}")
        print(f"{chi_calculado} < {chi_critico}")
    else:
        print(f"El generador de números aleatorios NO pasa la prueba de Chi-Cuadrada con el valor crítico: {chi_critico} y el valor calculado de: {chi_calculado}")
        print(f"{chi_calculado} > {chi_critico}")

def validar_aleatoriedad(numeros):
    while True:
        print("\nSeleccione la prueba estadística para validar la aleatoriedad:")
        print("1. Prueba de Kolmogorov-Smirnov")
        print("2. Prueba de Chi Cuadrada")
        print("3. Volver al menú principal")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            validar_kolmogorov(numeros)
            break
        elif choice == '2':
            validar_chi_cuadrada(numeros)
            break
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
