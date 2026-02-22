# Guía Accesible de Probabilidad y Estadística

## Descripción General

La presente aplicación corresponde a un sistema educativo de escritorio
desarrollado en Python, cuyo propósito es facilitar el aprendizaje de
los conceptos fundamentales de Probabilidad relacionados con el análisis
combinatorio.

El sistema integra teoría, cálculo automatizado, procesamiento de
archivos y herramientas de accesibilidad dentro de una única interfaz
gráfica desarrollada con Tkinter.

------------------------------------------------------------------------

## Objetivos del Proyecto

### Objetivo General

Desarrollar una aplicación interactiva que permita estudiar y aplicar
los conceptos de factorial, permutaciones y combinaciones mediante una
interfaz accesible y funcional.

### Objetivos Específicos

-   Implementar un motor matemático para el cálculo de operaciones
    combinatorias.
-   Incorporar contenido teórico embebido dentro del sistema.
-   Permitir el procesamiento masivo de operaciones mediante archivos
    .txt.
-   Exportar resultados en formato .csv.
-   Integrar herramientas de accesibilidad como lectura por voz y
    control de tamaño de fuente.
-   Implementar un sistema de reproducción musical como complemento
    ambiental.

------------------------------------------------------------------------

## Marco Teórico Integrado

La aplicación incluye contenido estructurado sobre:

-   Factorial
-   Permutaciones (orden importa)
-   Combinaciones (orden no importa)
-   Ejercicios resueltos
-   Bibliografía académica
-   Guía de uso del sistema

El contenido se encuentra embebido directamente en el código fuente
mediante estructuras tipo diccionario.

------------------------------------------------------------------------

## Arquitectura del Sistema

El sistema está estructurado bajo el paradigma de Programación Orientada
a Objetos (POO), organizado en las siguientes clases:

### 1. Clase Contenido

Almacena la información teórica organizada por secciones.

### 2. Clase MotorProbabilidad

Implementa los métodos matemáticos: - factorial(n) - permutacion(n, r) -
combinacion(n, r)

Utiliza la biblioteca estándar math para los cálculos factoriales.

### 3. Clase SistemaVoz

Permite la lectura del contenido mediante tecnología Text-To-Speech
utilizando la biblioteca pyttsx3 y ejecución en hilos independientes
(threading).

### 4. Clase SistemaMusica

Gestiona la reproducción de archivos MP3 utilizando la biblioteca
pygame.

### 5. Clase Aplicacion

Controla la interfaz gráfica desarrollada con Tkinter, organizando los
componentes mediante el sistema de distribución grid.

------------------------------------------------------------------------

## Funcionalidades Principales

### Calculadora Combinatoria

Permite calcular:

Permutación: P(n,r) = n! / (n-r)!

Combinación: C(n,r) = n! / (r!(n-r)!)

El resultado se muestra mediante ventanas emergentes.

------------------------------------------------------------------------

### Procesamiento de Archivos TXT

Formato requerido:

P,n,r 
C,n,r

El sistema procesa cada línea y genera resultados automáticamente.

------------------------------------------------------------------------

### Exportación a CSV

Los resultados pueden guardarse en formato CSV con las siguientes
columnas:

-   Operación
-   n
-   r
-   Resultado

Compatible con software de hojas de cálculo como Excel y LibreOffice.

------------------------------------------------------------------------

### Herramientas de Accesibilidad

-   Lectura por voz del contenido
-   Control de volumen independiente
-   Ajuste dinámico del tamaño de fuente
-   Interfaz maximizada automáticamente

------------------------------------------------------------------------

## Requisitos del Sistema

Python 3.10 o superior.

Dependencias externas:

pip install pyttsx3 pygame pillow

Tkinter se incluye por defecto en la mayoría de distribuciones de
Python.

------------------------------------------------------------------------

## Ejecución

python proba.py

------------------------------------------------------------------------

## Bibliografía

Devore, J. L. (2016). Probabilidad y Estadística para Ingeniería y
Ciencias. Cengage Learning.

Walpole, R. E., Myers, R. H. Probabilidad y Estadística para Ingenieros.
Pearson Educación.

Ross, S. M. Introducción a la Probabilidad. Academic Press.

------------------------------------------------------------------------

## Conclusión

La aplicación constituye una herramienta educativa integral que combina
teoría, práctica computacional y accesibilidad, permitiendo reforzar el
aprendizaje del análisis combinatorio mediante un entorno interactivo
desarrollado completamente en Python.
