"""Lógica de análisis combinatorio independiente de la interfaz gráfica."""

from __future__ import annotations

from math import comb, factorial, perm


class ErrorDeEntrada(ValueError):
    """Indica que una operación combinatoria recibió parámetros inválidos."""


def validar_parametros(n: int, r: int) -> None:
    """Valida los parámetros compartidos por permutaciones y combinaciones."""
    if not isinstance(n, int) or not isinstance(r, int):
        raise ErrorDeEntrada("n y r deben ser números enteros.")
    if n < 0:
        raise ErrorDeEntrada("n debe ser un entero no negativo.")
    if not 0 <= r <= n:
        raise ErrorDeEntrada("r debe estar entre 0 y n.")


def calcular_factorial(n: int) -> int:
    """Devuelve n! para un entero no negativo."""
    if not isinstance(n, int) or n < 0:
        raise ErrorDeEntrada("n debe ser un entero no negativo.")
    return factorial(n)


def calcular_permutacion(n: int, r: int) -> int:
    """Devuelve P(n, r), donde el orden de los elementos importa."""
    validar_parametros(n, r)
    return perm(n, r)


def calcular_combinacion(n: int, r: int) -> int:
    """Devuelve C(n, r), donde el orden de los elementos no importa."""
    validar_parametros(n, r)
    return comb(n, r)


def calcular(operacion: str, n: int, r: int) -> int:
    """Calcula una operación identificada por ``P`` o ``C``."""
    operaciones = {"P": calcular_permutacion, "C": calcular_combinacion}
    try:
        return operaciones[operacion.upper()](n, r)
    except KeyError as error:
        raise ErrorDeEntrada("La operación debe ser P (permutación) o C (combinación).") from error
