class ObjList:
    def __init__(self, data: str):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head is self.tail is None:
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.get_prev().set_next(None)
            self.tail = self.tail.get_prev()

    def get_data(self) -> list:
        data_list = []
        iterator = self.head
        while iterator is not None:
            data_list.append(iterator.get_data())
            iterator = iterator.get_next()
        return data_list
