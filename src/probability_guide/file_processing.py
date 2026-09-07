"""Batch calculation file processing and CSV export routines."""

from __future__ import annotations

import csv
from pathlib import Path

from .calculations import ErrorDeEntrada, InputError, calculate, calcular


def parse_lines(lines: list[str]) -> list[tuple[str, int, int, int]]:
    """Converts 'P,n,r' or 'C,n,r' lines into calculated results.

    Reports line numbers to ensure user input errors are easily diagnosable.
    """
    results = []
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 3:
            raise InputError(
                f"Línea {line_number}: se esperaba el formato P,n,r o C,n,r."
            )
        operation, text_n, text_r = parts
        try:
            n, r = int(text_n), int(text_r)
            result = calculate(operation, n, r)
        except ValueError as error:
            raise InputError(f"Línea {line_number}: {error}") from error
        results.append((operation.upper(), n, r, result))
    if not results:
        raise InputError("El archivo no contiene cálculos válidos.")
    return results


procesar_lineas = parse_lines


def parse_file(file_path: str | Path) -> list[tuple[str, int, int, int]]:
    """Reads a UTF-8 file containing operations."""
    with Path(file_path).open(encoding="utf-8") as file:
        return parse_lines(file.readlines())


procesar_archivo = parse_file


def export_csv(file_path: str | Path, results: list[tuple[str, int, int, int]]) -> None:
    """Saves calculation results with CSV headers compatible with Excel and LibreOffice."""
    with Path(file_path).open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Operacion", "n", "r", "Resultado"])
        writer.writerows(results)


exportar_csv = export_csv
