class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_left(self, weight):
        self.left_weight += weight

    def add_right(self, weight):
        self.right_weight += weight

    def result(self):
        if self.left_weight == self.right_weight:
            return '='
        elif self.left_weight > self.right_weight:
            return 'L'
        else:
            return 'R'


# Пример использования
balance = Balance()
balance.add_left(5)
balance.add_right(3)
print(balance.result())  # L

balance.add_right(2)
print(balance.result())  # =
