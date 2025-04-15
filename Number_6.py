class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value
        elif index in self.data:
            del self.data[index]

    def __getitem__(self, index):
        return self.data.get(index, 0)

    def __repr__(self):
        return str(self.data)


# Пример использования
arr = SparseArray()
arr[0] = 5
arr[3] = 10
print(arr[0])  # 5
print(arr[1])  # 0
print(arr)  # {0: 5, 3: 10}
arr[0] = 0  # удаляет элемент при присваивании нуля
print(arr)  # {3: 10}
