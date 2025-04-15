class NumberTransform:
    def __init__(self, numbers):
        self.numbers = list(map(int, numbers.split()))

    def make_negative(self):
        self.numbers = [num * -1 if num > 0 else num for num in self.numbers]

    def square(self):
        self.numbers = [num ** 2 for num in self.numbers]

    def strange_command(self):
        self.numbers = [num + 1 if num % 5 == 0 else num for num in self.numbers]

    def apply_command(self, command_name):
        commands = {
            "make_negative": self.make_negative,
            "square": self.square,
            "strange_command": self.strange_command
        }
        if command_name in commands:
            commands[command_name]()
        else:
            print("Ошибка: недопустимая команда.")

    def get_numbers(self):
        return self.numbers


# Пример использования
input_numbers = input("Введите числа через пробел: ")
transformer = NumberTransform(input_numbers)
transformer.apply_command("make_negative")  # Пример команды
print(transformer.get_numbers())
