class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [n for n in self.numbers if n % 2 != 0]

    def get_evens(self):
        return [n for n in self.numbers if n % 2 == 0]


# Пример использования
selector = Selector([1, 4, 5, 2, 7])
print(selector.get_odds())  # [1, 5, 7]
print(selector.get_evens())  # [4, 2]
