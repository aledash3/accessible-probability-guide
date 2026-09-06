"""Lectura y exportación de cálculos por lotes."""

from __future__ import annotations

import csv
from pathlib import Path

from .calculos import ErrorDeEntrada, calcular


def procesar_lineas(lineas: list[str]) -> list[tuple[str, int, int, int]]:
    """Convierte líneas ``P,n,r`` o ``C,n,r`` en resultados calculados.

    Informa el número de línea para que los errores del archivo sean fáciles de corregir.
    """
    resultados = []
    for numero_linea, linea in enumerate(lineas, start=1):
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        partes = [parte.strip() for parte in linea.split(",")]
        if len(partes) != 3:
            raise ErrorDeEntrada(
                f"Línea {numero_linea}: se esperaba el formato P,n,r o C,n,r."
            )
        operacion, texto_n, texto_r = partes
        try:
            n, r = int(texto_n), int(texto_r)
            resultado = calcular(operacion, n, r)
        except ValueError as error:
            raise ErrorDeEntrada(f"Línea {numero_linea}: {error}") from error
        resultados.append((operacion.upper(), n, r, resultado))
    if not resultados:
        raise ErrorDeEntrada("El archivo no contiene cálculos válidos.")
    return resultados


def procesar_archivo(ruta: str | Path) -> list[tuple[str, int, int, int]]:
    """Lee un archivo UTF-8 de operaciones."""
    with Path(ruta).open(encoding="utf-8") as archivo:
        return procesar_lineas(archivo.readlines())


def exportar_csv(ruta: str | Path, resultados: list[tuple[str, int, int, int]]) -> None:
    """Guarda resultados con encabezados aptos para Excel y LibreOffice."""
    with Path(ruta).open("w", newline="", encoding="utf-8-sig") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Operacion", "n", "r", "Resultado"])
        writer.writerows(resultados)
