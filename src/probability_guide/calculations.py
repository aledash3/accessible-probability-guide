"""Combinatorics computation engine independent of the graphical user interface."""

from __future__ import annotations

from math import comb, factorial, perm


class InputError(ValueError):
    """Indicates that a combinatorics operation received invalid parameters."""


# Backward compatibility alias
ErrorDeEntrada = InputError


def validate_parameters(n: int, r: int) -> None:
    """Validates shared constraints for permutations and combinations."""
    if not isinstance(n, int) or not isinstance(r, int):
        raise InputError("n y r deben ser números enteros.")
    if n < 0:
        raise InputError("n debe ser un entero no negativo.")
    if not 0 <= r <= n:
        raise InputError("r debe estar entre 0 y n.")


validar_parametros = validate_parameters


def calculate_factorial(n: int) -> int:
    """Returns n! for a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise InputError("n debe ser un entero no negativo.")
    return factorial(n)


calcular_factorial = calculate_factorial


def calculate_permutation(n: int, r: int) -> int:
    """Returns P(n, r), where element order matters."""
    validate_parameters(n, r)
    return perm(n, r)


calcular_permutacion = calculate_permutation


def calculate_combination(n: int, r: int) -> int:
    """Returns C(n, r), where element order does not matter."""
    validate_parameters(n, r)
    return comb(n, r)


calcular_combinacion = calculate_combination


def calculate(operation: str, n: int, r: int) -> int:
    """Calculates an operation identified by 'P' or 'C'."""
    operations = {"P": calculate_permutation, "C": calculate_combination}
    try:
        return operations[operation.upper()](n, r)
    except KeyError as error:
        raise InputError("La operación debe ser P (permutación) o C (combinación).") from error


calcular = calculate
