class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        count = 0
        for i in range(N + 1):
            count += self.transform(int(i))
        return count


class SquareSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 3


# Пример использования:
summator = Summator()
print(summator.sum(3))  # Выводит 6 (1 + 2 + 3)

square_summator = SquareSummator()
print(square_summator.sum(3))  # Выводит 14 (1^2 + 2^2 + 3^2)

cube_summator = CubeSummator()
print(cube_summator.sum(3))  # Выводит 36 (1^3 + 2^3 + 3^3)
