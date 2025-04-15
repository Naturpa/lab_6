class BigBell:
    def __init__(self):
        self.is_ding = True

    def sound(self):
        if self.is_ding:
            print("ding")
        else:
            print("dong")
        self.is_ding = not self.is_ding


# Пример использования
bell = BigBell()
bell.sound()  # Вывод: ding
bell.sound()  # Вывод: dong
bell.sound()  # Вывод: ding
bell.sound()  # Вывод: dong
