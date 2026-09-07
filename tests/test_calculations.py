import unittest

from probability_guide.calculations import (
    ErrorDeEntrada,
    InputError,
    calculate,
    calculate_combination,
    calculate_factorial,
    calculate_permutation,
    calcular_combinacion,
    calcular_factorial,
    calcular_permutacion,
)
from probability_guide.file_processing import parse_lines, procesar_lineas


class CombinatoricsCalculationTests(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calcular_factorial(5), 120)

    def test_permutation(self):
        self.assertEqual(calculate_permutation(9, 3), 504)
        self.assertEqual(calcular_permutacion(9, 3), 504)

    def test_combination(self):
        self.assertEqual(calculate_combination(9, 5), 126)
        self.assertEqual(calcular_combinacion(9, 5), 126)

    def test_generic_calculate(self):
        self.assertEqual(calculate("P", 5, 2), 20)
        self.assertEqual(calculate("C", 5, 2), 10)

    def test_rejects_r_greater_than_n(self):
        with self.assertRaisesRegex(InputError, "entre 0 y n"):
            calculate_combination(3, 4)

    def test_parses_lines_and_comments(self):
        result = parse_lines(["# sample comment", "P, 5, 3", "C,7,2"])
        self.assertEqual(result, [("P", 5, 3, 60), ("C", 7, 2, 21)])

    def test_reports_invalid_line_number(self):
        with self.assertRaisesRegex(ErrorDeEntrada, "Línea 2"):
            parse_lines(["P,5,2", "X,4,2"])


if __name__ == "__main__":
    unittest.main()
