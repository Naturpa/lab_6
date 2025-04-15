class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Стороны не образуют треугольник")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length)


# Пример использования:
triangle = Triangle(3, 4, 5)
print(triangle.perimeter())  # Выводит 12

equilateral = EquilateralTriangle(5)
print(equilateral.perimeter())  # Выводит 15
