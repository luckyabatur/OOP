class FloatValue:
    @staticmethod
    def float_check(value):
        return isinstance(value, float)

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not self.float_check(value):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell(0.0) for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
value = 1.0
for line in table.cells:
    for cell in line:
        cell.value = value
        value += 1.0
