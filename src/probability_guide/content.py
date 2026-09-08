"""Contenido pedagógico de la guía de análisis combinatorio (Bilingüe ES / EN)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    title: str
    icon: str
    summary: str
    content: str
    image: str | None = None

    @property
    def titulo(self) -> str:
        return self.title

    @property
    def icono(self) -> str:
        return self.icon

    @property
    def resumen(self) -> str:
        return self.summary

    @property
    def contenido(self) -> str:
        return self.content

    @property
    def imagen(self) -> str | None:
        return self.image


Leccion = Lesson


LECCIONES_ES = (
    Lesson(
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
    Lesson(
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
    Lesson(
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
    Lesson(
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
    Lesson(
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
    Lesson(
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
    Lesson(
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
    Lesson(
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


LESSONS_EN = (
    Lesson(
        "Welcome",
        "⌂",
        "Start by recognizing when order matters in counting.",
        """COMBINATORICS & PROBABILITY FOUNDATIONS

Combinatorics allows us to count possibilities efficiently without enumerating them one by one. In this guide you will master three core concepts:

• Factorial: the mathematical foundation for arranging items.
• Permutations: order changes the outcome.
• Combinations: order does not change the outcome.

Recommended Learning Path

1. Read the decision rule.
2. Review the factorial operation.
3. Compare permutations with combinations.
4. Practice with the interactive calculator and exercises.

Tip: Before choosing a formula, ask yourself if A-B is distinct from B-A. If yes, order likely matters.""",
    ),
    Lesson(
        "Decision Rule",
        "?",
        "A quick mental check to pick the right formula.",
        """PERMUTATION OR COMBINATION?

Use a PERMUTATION when order, rank, or position is relevant.
Examples: race podium, passwords/PINs, seat assignments, president and secretary roles.

Use a COMBINATION when only the group membership matters.
Examples: committee members, cards in a hand, sample of students selected.

Mental Test

Is the group {Ana, Luis} distinct from {Luis, Ana}?

• Yes: order matters → Permutation.
• No: order does not matter → Combination.

Both formulas require 0 ≤ r ≤ n, where n represents available elements and r represents selected elements.""",
    ),
    Lesson(
        "Factorial",
        "!",
        "The product of all positive integers up to n.",
        """FACTORIAL

Definition
n! = n · (n − 1) · (n − 2) · … · 1

Important Special Cases
0! = 1
1! = 1
5! = 5 · 4 · 3 · 2 · 1 = 120

Interpretation

If you have n distinct objects and want to arrange all of them in a sequence, there are n! distinct ways to do so. For example, three books A, B, and C can be arranged in 3! = 6 different ways.

Factorials grow extremely fast. Avoid calculating them by hand for large numbers and use this application's calculator.""",
        "factorial.png",
    ),
    Lesson(
        "Permutations",
        "P",
        "Selections where each position and rank counts.",
        """PERMUTATIONS

Formula
P(n, r) = n! / (n − r)!

A permutation selects r items from n available elements and orders them. Changing the order produces a different outcome.

Example

From 9 candidates, in how many ways can 1st (gold), 2nd (silver), and 3rd (bronze) medals be awarded?

P(9, 3) = 9! / (9 − 3)! = 9! / 6! = 9 · 8 · 7 = 504

Selecting Ana–Luis–Marta is NOT the same as Luis–Ana–Marta: the medal podium changes. That is why a permutation is required.""",
        "permutacion.png",
    ),
    Lesson(
        "Combinations",
        "C",
        "Selections where group membership matters, not order.",
        """COMBINATIONS

Formula
C(n, r) = n! / [r! · (n − r)!]

A combination chooses r elements from n available items without regard to their order.

Example

How many 5-card hands can be dealt from a subset of 9 cards?

C(9, 5) = 9! / [5! · 4!] = 126

The group {A, B, C, D, E} represents the exact same hand regardless of the sequence in which cards were dealt. That is why a combination is used.""",
        "combinaciones.png",
    ),
    Lesson(
        "Guided Exercises",
        "✦",
        "Practice identifying data, order, and formulas.",
        """GUIDED EXERCISES

1. Arrange 4 distinct books on a shelf
All books change position, so order matters.
P(4, 4) = 4! = 24

2. Choose 2 representatives from 5 students
Only the identity of the chosen students matters.
C(5, 2) = 10

3. Create a 3-character distinct password from 7 symbols
ABC and BAC are distinct passwords.
P(7, 3) = 7 · 6 · 5 = 210

4. Form a committee of 3 people from 8 candidates
The committee of Ana, Luis, and Marta is identical regardless of selection order.
C(8, 3) = 56

Verify each calculation in the right-hand calculator panel.""",
    ),
    Lesson(
        "Batch Processing",
        "↥",
        "Process large problem sets and export structured reports.",
        """BATCH PROCESSING

The application accepts plain text (.txt) files containing one operation per line.

Format
P,n,r
C,n,r

Example
# Operation,n,r
P,6,5
C,6,5

You can include blank lines and comments starting with '#'. When loading a file, the application validates each line and reports exact line numbers if formatting errors occur.

You can then export the computed results directly as a CSV file for Excel, Google Sheets, or LibreOffice.""",
    ),
    Lesson(
        "Bibliography",
        "⌁",
        "Academic references for further study.",
        """BIBLIOGRAPHY & REFERENCES

1. Devore, J. L. (2016). Probability and Statistics for Engineering and the Sciences. Cengage Learning.

2. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. Probability & Statistics for Engineers & Scientists. Pearson Education.

3. Ross, S. M. Introduction to Probability Models. Academic Press.

4. Course lecture notes — Universidad Politécnica Salesiana.

This guide is an educational companion and does not replace primary academic literature or reasoned problem-solving practice.""",
    ),
)


def get_lessons(language: str = "es") -> tuple[Lesson, ...]:
    """Retorna el catálogo de lecciones según el idioma ('es' o 'en')."""
    if str(language).lower().startswith("en"):
        return LESSONS_EN
    return LECCIONES_ES


LECCIONES = LECCIONES_ES
LESSONS = LESSONS_EN
