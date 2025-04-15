class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __add__(self, other):
        # Уравниваем длины списков коэффициентов
        length = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [0] * length

        for i in range(length):
            if i < len(self.coefficients):
                new_coefficients[i] += self.coefficients[i]
            if i < len(other.coefficients):
                new_coefficients[i] += other.coefficients[i]

        return Polynomial(new_coefficients)

    def __repr__(self):
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(self.coefficients))


# Пример использования
poly1 = Polynomial([1, 2, 3])  # 1 + 2x + 3x^2
poly2 = Polynomial([0, 1, 4])  # 0 + 1x + 4x^2

print(poly1(2))  # Значение poly1 при x=2
poly_sum = poly1 + poly2
print(poly_sum)  # Результат сложения многочленов
