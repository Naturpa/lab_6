class A:
    def __str__(self):
        return 'A.str method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return 'B.str method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    pass


class D(B, A):
    pass


# Пример использования:
c = C()
d = D()
print(str(c))  # 'A.str method'
print(str(d))  # 'B.str method'
