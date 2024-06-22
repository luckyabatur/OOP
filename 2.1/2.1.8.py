class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_coords(self) -> tuple:
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if all(isinstance(args[i], Point) for i in range(len(args))):
            self.__sp = args[0]
            self.__ep = args[1]
        elif all(isinstance(args[i], (int, float)) for i in range(len(args))):
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            raise TypeError

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: ({self.__sp.get_coords()[0]}, '
              f'{self.__sp.get_coords()[1]}) ({self.__ep.get_coords()[0]}, '
              f'{self.__ep.get_coords()[1]})')


rect = Rectangle(0, 0, 20, 34)
