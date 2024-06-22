class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def set_coords(self, x1: int, y1: int, x2: int, y2: int):
        if all(isinstance(x, int) for x in (x1, y1, x2, y2)):
            self.__x1 = x1
            self.__x2 = x2
            self.__y1 = y1
            self.__y2 = y2
        else:
            raise TypeError

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(' '.join([str(x) for x in self.get_coords()]))

