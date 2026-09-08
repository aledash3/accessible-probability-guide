import unittest
from probability_guide.content import LECCIONES_ES, LESSONS_EN, get_lessons, Lesson


class ContentBilingualTests(unittest.TestCase):
    def test_spanish_curriculum(self):
        lessons = get_lessons("es")
        self.assertEqual(len(lessons), 8)
        self.assertEqual(lessons[0].title, "Bienvenida")
        self.assertEqual(lessons[2].title, "Factorial")
        self.assertEqual(lessons[2].image, "factorial.png")
        self.assertEqual(lessons[3].title, "Permutaciones")
        self.assertEqual(lessons[3].image, "permutacion.png")
        self.assertEqual(lessons[4].title, "Combinaciones")
        self.assertEqual(lessons[4].image, "combinaciones.png")

    def test_english_curriculum(self):
        lessons = get_lessons("en")
        self.assertEqual(len(lessons), 8)
        self.assertEqual(lessons[0].title, "Welcome")
        self.assertEqual(lessons[2].title, "Factorial")
        self.assertEqual(lessons[2].image, "factorial.png")
        self.assertEqual(lessons[3].title, "Permutations")
        self.assertEqual(lessons[3].image, "permutacion.png")
        self.assertEqual(lessons[4].title, "Combinations")
        self.assertEqual(lessons[4].image, "combinaciones.png")

    def test_lesson_backward_compatibility_properties(self):
        l = Lesson(title="T", icon="*", summary="S", content="C", image="img.png")
        self.assertEqual(l.titulo, "T")
        self.assertEqual(l.icono, "*")
        self.assertEqual(l.resumen, "S")
        self.assertEqual(l.contenido, "C")
        self.assertEqual(l.imagen, "img.png")


if __name__ == "__main__":
    unittest.main()
