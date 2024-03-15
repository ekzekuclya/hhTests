import unittest
from main import ShapeDetector, GeometryCalculator


class TestShapeDetector(unittest.TestCase):
    def test_detect_shape_circle(self):
        self.assertEqual(ShapeDetector.detect_shape(5), "circle")

    def test_detect_shape_triangle(self):
        self.assertEqual(ShapeDetector.detect_shape(3, 4, 5), "triangle")

    def test_detect_shape_unknown(self):
        self.assertEqual(ShapeDetector.detect_shape(1, 2), "unknown")


class TestGeometryCalculator(unittest.TestCase):
    def test_is_right_triangle_true(self):
        self.assertTrue(GeometryCalculator.is_right_triangle(3, 4, 5))

    def test_is_right_triangle_false(self):
        self.assertFalse(GeometryCalculator.is_right_triangle(2, 3, 4))

    def test_is_right_triangle_invalid_input(self):
        with self.assertRaises(ValueError):
            GeometryCalculator.is_right_triangle(0, 3, 4)

    def test_area_circle(self):
        self.assertAlmostEqual(GeometryCalculator.area(5), 78.54, places=2)

    def test_area_triangle(self):
        self.assertAlmostEqual(GeometryCalculator.area(3, 4, 5), 6.0)

    def test_area_invalid_input(self):
        with self.assertRaises(ValueError):
            GeometryCalculator.area(-1, 2, 3)

if __name__ == '__main__':
    unittest.main()




