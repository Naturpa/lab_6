class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other


# Пример использования
a = Point(1, 2)
b = Point(1, 2)
c = Point(3, 4)
print(a == b)  # True
print(a != c)  # True
