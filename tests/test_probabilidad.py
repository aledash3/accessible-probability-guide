import unittest

from guia_probabilidad.calculos import (
    ErrorDeEntrada,
    calcular_combinacion,
    calcular_factorial,
    calcular_permutacion,
)
from guia_probabilidad.archivos import procesar_lineas


class CalculosCombinatoriosTests(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(calcular_factorial(5), 120)

    def test_permutacion(self):
        self.assertEqual(calcular_permutacion(9, 3), 504)

    def test_combinacion(self):
        self.assertEqual(calcular_combinacion(9, 5), 126)

    def test_rechaza_r_mayor_que_n(self):
        with self.assertRaisesRegex(ErrorDeEntrada, "entre 0 y n"):
            calcular_combinacion(3, 4)

    def test_procesa_lineas_y_comentarios(self):
        resultado = procesar_lineas(["# ejemplo", "P, 5, 3", "C,7,2"])
        self.assertEqual(resultado, [("P", 5, 3, 60), ("C", 7, 2, 21)])

    def test_informa_linea_incorrecta(self):
        with self.assertRaisesRegex(ErrorDeEntrada, "Línea 2"):
            procesar_lineas(["P,5,2", "X,4,2"])


if __name__ == "__main__":
    unittest.main()
