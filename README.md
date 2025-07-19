# Simulación de Números Aleatorios y Variables Aleatorias
Este proyecto en Python permite generar secuencias de números aleatorios mediante diferentes métodos, validar su aleatoriedad mediante pruebas estadísticas, y extraer variables aleatorias discretas y continuas.

## Estructura del Proyecto
* `main.py`: menú principal y flujo de navegación.
* `Generadores.py`: implementa métodos de generación de números aleatorios (Congruencial Mixto, Multiplicativo, Cuadrado Medio).
* `Validaciones.py`: incluye pruebas estadísticas como:
    * Chi Cuadrada
    * Kolmogorov-Smirnov
    * Test de Rachas
    * Ljung-Box
* `VariablesAleatorias.py`: implementación de:
    * Transformada Inversa 
    * Método de Aceptación-Rechazo

## Funcionalidades
### 1. Generación de Números Aleatorios

  * Método Congruencial Lineal Mixto
  * Método Congruencial Lineal Multiplicativo
  * Método del Cuadrado Medio
  * Comparación de períodos entre generadores

### 2. Validación de Aleatoriedad

* Pruebas estadisticas para evaluar uniformidad e independencia:
  * Chi Cuadrada
  * Kolmogorov-Smirnov
  * Test de Rachas
  * Test Ljung-Box

### 3. Extracción de Variables Aleatorias

* Transformada inversa para variables discreta (según frecuencias observadas)
* Método de Aceptación-Rechazo con función de densidad lineal

## Ejecución
#### 1. Instalar las dependencias:

   pip install sympy scipy pandas statsmodels tabulate

#### 2. Ejecutar el programa:

   python main.py
  
## Objetivo del Proyecto

Este programa fue desarrollado como proyecto final de la materia **Simulación**, perteneciente a la carrera de **Ingeniería en Sistemas de Información**.

## Dependencias

* `sympy`: para validaciones matemáticas (primalidad, etc).
* `tabulate`: visualización tabular en consola.
* `scipy`, `statsmodels`: para pruebas estadísticas.
* `pandas`: procesamiento de resultados.

## ✍️ Autor

Desarrollado por Julieta Lorenzo para prácticas académicas en Simulación.

