from sympy import isprime, factorint
from tabulate import tabulate


def ValidarModulo():
    while True:
      x = int(input("Ingrese el valor del modulo: "))
      if (x > 0):
        return x
      else:
        print("Error. Ingrese un valor de modulo mayor a cero")

def ValidarSemilla():
    while True:
      x = int(input("Ingrese un valor de semilla: "))
      if (x > 0):
        return x
      else:
        print("Error. Ingrese un valor de semilla mayor a cero")

def ValidarMultiplicador(m):
    while True:
      a = int(input("Ingrese el valor del multiplicador: "))
      if (0 < a < m):
        return a
      else:
        print("Error. Ingrese un valor de multiplicador mayor a cero y menor al modulo")

def ValidarIncremento(m):
  while True:
    b = int(input("Ingrese un valor de la constante aditiva: "))
    if (0 <= b < m):
      return b
    else:
      print("Incorrecto. Ingrese un valor de constante aditiva mayor o igual a 0 y menor al modulo")

def cicloCompleto(periodo, m):
    if (periodo == m):
        print("El generador es de ciclo completo")
    else:
        print("El generador es de ciclo incompleto")


def ValidarModuloEsPrimo(m):
    if isprime(m):
        return True
    else:
        return False

def SecuenciaMaxima(a, m):
    factorizar = factorint(m-1)
    lista_fprimos = list(factorizar.keys())
    contador = 0

    for p in lista_fprimos:
      calculo = (a ** ((m - 1) /p)) % m
      if (calculo == 1):
        contador = contador + 1

    if (contador > 0):
      print("\nEl Generador no cumple con la condicion de que el Multiplicativo a sea una raíz primitiva de m. Por lo tanto, no podra alcanzar la maxima secuencia.")

    else:
      print("\nEl Generador cumple con todas las condiciones. Puede alcanzar la maxima secuencia")


def validarSecuenciaMaxima(a,m):
    print("\nDesea validar si el Generador cumple con las condiciones para alcanzar la Secuencia Maxima?")
    validar = input("Ingrese SI o NO: ").strip().upper()

    if (validar == "SI"):
        if (ValidarModuloEsPrimo(m)):
            SecuenciaMaxima(a,m)
        else:
            print("El Generador no cumple con la condicion de que el valor del Modulo sea un numero primo. Por lo tanto, no podra alcanzar la secuencia maxima")

def ValidarCantidadDigitos():
  while True:
    d = int(input("Ingrese la cantidad de digitos: "))
    if (d > 0):
      return d

def ValidarLongitudSemilla(d):
    x = ValidarSemilla()
    if len(str(x)) != d:
        print("El valor de la semilla debe ser de " + str(d) + " digitos")
        ValidarLongitudSemilla(d)
    return x

def LongitudNumeroAlCuadrado(d):
    maximoNum = "9"*d
    maximoNumCuadrado = int(maximoNum) ** 2
    longitudNumCuadrado = len(str(maximoNumCuadrado))

    return longitudNumCuadrado

def TomarParteCentral(x2, l_max, d):
    numero_str = str(x2)

    inicio = int((l_max - d) / 2)
    fin = int(inicio + d)

    parte_central = numero_str[inicio:fin]

    return int(parte_central)

def SeRepite(numeros, nuevo_num):
  if nuevo_num in numeros:
    return True
  else:
    return False


def MetodoConguencialMixto():
    print("\nMetodo Congruencial Lineal Mixto")
    m = ValidarModulo()
    x = ValidarSemilla()
    a = ValidarMultiplicador(m)
    b = ValidarIncremento(m)

    periodo = 0
    bandera = False

    numeros = []
    results = []
    numeros_aleatorios = []

    while(bandera == False):
        if (periodo == 0):
            numeros.append(x)

        num_aleatorio = round(x / m, 3)
        results.append((periodo + 1, num_aleatorio))
        numeros_aleatorios.append(num_aleatorio)

        x = ((a * x) + b) % m

        if SeRepite(numeros, x):
            bandera = True
        else:
            numeros.append(x)

        periodo += 1

    print("\nNumeros Aleatorios generados:")
    print(tabulate(results, headers=["i", "Numero Aleatorio u"], tablefmt="grid", colalign=("center", "center")))

    print("\nLongitud de Periodo = ", periodo)
    cicloCompleto(periodo, m)

    return numeros_aleatorios

def MetodoConguencialMixtoComparacion():
    m = ValidarModulo()
    x = ValidarSemilla()
    a = ValidarMultiplicador(m)
    b = ValidarIncremento(m)

    periodo = 0
    bandera = 0

    while(bandera != x):
        if (periodo == 0):
            bandera = x

        x = ((a * x) + b) % m
        periodo += 1
        num_aleatorio = x / m

        if (bandera == x):
            break
    return periodo

def MetodoCongruencialMultiplicativo():
    print("\nMetodo Congruencial Lineal Multiplicativo")
    m = ValidarModulo()
    x = ValidarSemilla()
    a = ValidarMultiplicador(m)

    periodo = 0
    bandera = False

    numeros = []
    results = []
    numeros_aleatorios = []

    while(bandera == False):
        if (periodo == 0):
            numeros.append(x)

        num_aleatorio = round(x / m, 3)
        results.append((periodo + 1, num_aleatorio))
        numeros_aleatorios.append(num_aleatorio)

        x = (a * x) % m

        if SeRepite(numeros, x):
            bandera = True
        else:
            numeros.append(x)

        periodo += 1

    print("\nNumeros Aleatorios generados:")
    print(tabulate(results, headers=["i", "Numero Aleatorio u"], tablefmt="grid", colalign=("center", "center")))

    validarSecuenciaMaxima(a,m)
    print("\nLongitud de Periodo = ", periodo)

    return numeros_aleatorios


def MetodoCongruencialMultiplicativoComparacion():
    m = ValidarModulo()
    x = ValidarSemilla()
    a = ValidarMultiplicador(m)

    periodo = 0
    bandera = 0
    num_aleatorio = x / m


    while(bandera != x):
        if (periodo == 0):
            bandera = x
        x = (a * x) % m
        periodo += 1
        num_aleatorio = x / m

        if (bandera == x):
            break
    return periodo


def MetodoDelCuadradoMedio():
    print("\nMetodo del Cuadrado Medio")
    d = ValidarCantidadDigitos()
    x = ValidarLongitudSemilla(d)

    l_max = LongitudNumeroAlCuadrado(d)
    normalizar = 10 ** d
    numeros = []
    results = []
    numeros_aleatorios = []

    periodo = 0
    bandera = False

    while (bandera == False):
      if periodo == 0:
        numeros.append(x)

      x2= x**2
      l_x2 = len(str(x2))

      if l_x2 < l_max:
        diferencia_l = l_max-l_x2
        x2 = x2 * (10 ** diferencia_l)

      num_central = TomarParteCentral(x2, l_max, d)
      num_aleatorio = x / normalizar

      results.append((periodo + 1, num_aleatorio))
      numeros_aleatorios.append(num_aleatorio)

      if SeRepite(numeros, num_central):
        bandera = True
      else:
        numeros.append(num_central)

      periodo = periodo + 1
      x = num_central

      if x == 0:
          break

    print(tabulate(results, headers=["i", "Numero Aleatorio u"], tablefmt="grid", colalign=("center", "center")))

    print("\nLongitud del Periodo = ", periodo)

    return numeros_aleatorios

def MetodoDelCuadradoMedioComparacion():
    d = ValidarCantidadDigitos()
    x = ValidarLongitudSemilla(d)

    l_max = LongitudNumeroAlCuadrado(d)
    normalizar = 10 ** d
    numeros = []

    periodo = 0
    bandera = False

    while (bandera == False):
      if periodo == 0:
        numeros.append(x)

      x2= x**2
      l_x2 = len(str(x2))

      if l_x2 < l_max:
        diferencia_l = l_max-l_x2
        x2 = x2 * (10 ** diferencia_l)

      num_central = TomarParteCentral(x2, l_max, d)
      num_aleatorio = x / normalizar

      if SeRepite(numeros, num_central):
        bandera = True
      else:
        numeros.append(num_central)

      periodo = periodo + 1
      x = num_central

      if x == 0:
          break

    return periodo

def compararGeneradores():
    print("\nMetodos para realizar la comparacion")

    print("\n1. Método Congruencial Lineal Mixto")
    print("2. Método Congruencial Lineal Multiplicativo")
    print("3. Método del Cuadrado Medio")

    metodo = input("\nIngrese el numero correspondiente al Metodo elegido: ")
    periodo1 = 0
    periodo2 = 0

    if metodo == '1':
        print("\nMétodo Congruencial Lineal Mixto")
        print("\nIngrese el valor de los parametros para el primer generador")
        periodo1 = MetodoConguencialMixtoComparacion()
        print("\nIngrese el valor de los parametros para el segundo generador")
        periodo2 = MetodoConguencialMixtoComparacion()

    elif metodo == '2':
        print("\nMétodo Congruencial Lineal Multiplicativo")
        print("\nIngrese el valor de los parametros para el primer generador")
        periodo1 = MetodoCongruencialMultiplicativoComparacion()
        print("\nIngrese el valor de los parametros para el segundo generador")
        periodo2 = MetodoCongruencialMultiplicativoComparacion()

    elif metodo == '3':
        print("\nMétodo del Cuadrado Medio")
        print("\nIngrese el valor de los parametros para el primer generador")
        periodo1 = MetodoDelCuadradoMedioComparacion()
        print("\nIngrese el valor de los parametros para el segundo generador")
        periodo2 = MetodoDelCuadradoMedioComparacion()

    else:
        print("Opción no válida. Por favor, intente de nuevo.")

    print("\nEl primer generador tiene un periodo igual a " + str(periodo1))
    print("El segundo generador tiene un periodo igual a " + str(periodo2))

    if (periodo1 > periodo2):
        print("\nEl primer Generador alcanza una mayor longitud de periodo")
    elif (periodo1 < periodo2):
        print("\nEl segundo Generador alcanza una mayor longitud de periodo")
    else:
        print("\nAmbos Generadores alcanzan la misma longitud de periodo")



