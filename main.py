import math


class ShapeDetector:
    @staticmethod
    def detect_shape(*args):
        if len(args) == 1:
            return "circle"
        elif len(args) == 3:
            return "triangle"
        else:
            return "unknown"


class GeometryCalculator:
    @staticmethod
    def is_right_triangle(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Все стороны треугольника должны быть больше нуля")
        sides = sorted([a, b, c])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

    @staticmethod
    def area(*args):
        if any(arg <= 0 for arg in args):
            raise ValueError("Все аргументы должны быть больше нуля")

        shape_type = ShapeDetector.detect_shape(*args)
        if shape_type == "circle":
            radius = args[0]
            area = math.pi * radius ** 2
            print("Площадь круга:", area)
            return area
        elif shape_type == "triangle":
            a, b, c = args
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            print("Площадь треугольника:", area)
            return area
        else:
            return None

