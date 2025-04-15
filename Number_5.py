class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, index):
        return self.lst[-(index + 1)]

    def __len__(self):
        return len(self.lst)


# Пример использования
rl = ReversedList([1, 2, 3, 4])
print(rl[0])  # 4
print(rl[1])  # 3
print(len(rl))  # 4
