"""Contenido pedagógico de la guía de análisis combinatorio."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Leccion:
    titulo: str
    icono: str
    resumen: str
    contenido: str
    imagen: str | None = None


LECCIONES = (
    Leccion(
        "Bienvenida",
        "⌂",
        "Empieza por reconocer cuándo importa el orden.",
        """ANÁLISIS COMBINATORIO

El análisis combinatorio permite contar posibilidades sin tener que enumerarlas una por una. En esta guía aprenderás tres ideas clave:

• Factorial: la base para organizar elementos.
• Permutaciones: el orden sí cambia el resultado.
• Combinaciones: el orden no cambia el resultado.

Ruta recomendada

1. Lee la regla de decisión.
2. Revisa factorial.
3. Compara permutaciones con combinaciones.
4. Practica con la calculadora y los ejercicios.

Consejo: antes de elegir una fórmula, pregúntate si A-B es distinto de B-A. Si la respuesta es sí, probablemente el orden importa.""",
    ),
    Leccion(
        "Regla de decisión",
        "?",
        "Una pregunta corta para escoger la fórmula correcta.",
        """¿PERMUTACIÓN O COMBINACIÓN?

Usa una PERMUTACIÓN cuando el orden o el puesto es relevante.
Ejemplos: podio de una carrera, claves, asientos, cargos de presidente y secretario.

Usa una COMBINACIÓN cuando solo interesa quiénes fueron elegidos.
Ejemplos: equipo de trabajo, cartas en una mano, grupo de estudiantes seleccionado.

Prueba mental

¿El grupo {Ana, Luis} es diferente de {Luis, Ana}?

• Sí: el orden importa → permutación.
• No: el orden no importa → combinación.

Las dos fórmulas requieren que 0 ≤ r ≤ n; n representa los elementos disponibles y r los elementos elegidos.""",
    ),
    Leccion(
        "Factorial",
        "!",
        "El producto de los enteros positivos hasta n.",
        """FACTORIAL

Definición
n! = n · (n − 1) · (n − 2) · … · 1

Casos importantes
0! = 1
1! = 1
5! = 5 · 4 · 3 · 2 · 1 = 120

Interpretación

Si tienes n objetos distintos y quieres ordenarlos todos, existen n! maneras de hacerlo. Por ejemplo, tres libros A, B y C se pueden ordenar de 3! = 6 formas.

El factorial crece muy rápido. Evita calcularlo manualmente para números grandes y usa la calculadora de esta aplicación.""",
        "factorial.png",
    ),
    Leccion(
        "Permutaciones",
        "P",
        "Selecciones en las que cada posición cuenta.",
        """PERMUTACIONES

Fórmula
P(n, r) = n! / (n − r)!

Una permutación selecciona r elementos de n y los ordena. Cambiar el orden crea un resultado diferente.

Ejemplo

De 9 estudiantes, ¿cuántas formas hay de asignar oro, plata y bronce?

P(9, 3) = 9! / 6! = 9 · 8 · 7 = 504

La elección Ana–Luis–Marta no es igual que Luis–Ana–Marta: el podio cambia. Por eso se usa una permutación.""",
        "permutacion.png",
    ),
    Leccion(
        "Combinaciones",
        "C",
        "Selecciones en las que importa el grupo, no su orden.",
        """COMBINACIONES

Fórmula
C(n, r) = n! / [r! · (n − r)!]

Una combinación elige r elementos de n sin ordenar sus posiciones.

Ejemplo

¿Cuántas manos de 5 cartas se pueden formar con 9 cartas?

C(9, 5) = 9! / [5! · 4!] = 126

El grupo {A, B, C, D, E} representa la misma mano sin importar en qué orden se nombraron las cartas. Por eso se usa una combinación.""",
        "combinaciones.png",
    ),
    Leccion(
        "Ejercicios guiados",
        "✦",
        "Practica identificando datos, orden y fórmula.",
        """EJERCICIOS GUIADOS

1. Ordenar 4 libros distintos

Todos los libros cambian de posición, así que el orden importa.
P(4, 4) = 4! = 24

2. Elegir 2 representantes de 5 estudiantes

Solo interesa quiénes quedan seleccionados.
C(5, 2) = 10

3. Crear una clave de 3 símbolos distintos a partir de 7

ABC y BAC son claves distintas.
P(7, 3) = 7 · 6 · 5 = 210

4. Formar un comité de 3 personas entre 8

El comité de Ana, Luis y Marta es el mismo sin importar el orden.
C(8, 3) = 56

Comprueba cada resultado en el panel de cálculo.""",
    ),
    Leccion(
        "Trabajo con archivos",
        "↥",
        "Procesa muchos ejercicios y exporta sus resultados.",
        """PROCESAMIENTO POR LOTES

La aplicación admite archivos TXT con una operación por línea.

Formato
P,n,r
C,n,r

Ejemplo
# Operación,n,r
P,6,5
C,6,5

Puedes incluir líneas vacías y comentarios que empiecen por #. Al cargar el archivo, la aplicación valida cada línea y muestra dónde está el problema si encuentra un formato incorrecto.

Después podrás guardar los resultados como CSV para abrirlos en Excel o LibreOffice.""",
    ),
    Leccion(
        "Bibliografía",
        "⌁",
        "Fuentes para profundizar después de la guía.",
        """BIBLIOGRAFÍA

1. Devore, J. L. (2016). Probabilidad y Estadística para Ingeniería y Ciencias. Cengage Learning.

2. Walpole, R. E., Myers, R. H., Myers, S. L. y Ye, K. Probabilidad y Estadística para Ingenieros. Pearson Educación.

3. Ross, S. M. Introducción a la Probabilidad. Academic Press.

4. Apuntes de clase de la Universidad Politécnica Salesiana.

La guía es un apoyo de estudio y no reemplaza las fuentes académicas ni la práctica razonada de los ejercicios.""",
    ),
)
