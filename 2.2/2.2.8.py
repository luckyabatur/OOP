from typing import Optional


class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    @classmethod
    def find_node(cls, node: TreeObj, indx):
        if node is None:
            return node
        if node.indx == indx:
            return node
        found = cls.find_node(node.left, indx)
        if found is None:
            found = cls.find_node(node.right, indx)
        return found

    @classmethod
    def predict(cls, root: TreeObj, x):
        if root.value is not None:
            return root.value
        if x[root.indx]:
            return cls.predict(root.left, x)
        else:
            return cls.predict(root.right, x)

    @staticmethod
    def add_obj(obj: TreeObj, node: Optional[TreeObj] = None, left: bool = True):
        if node is None:
            return obj
        if left:
            node.left = obj
        else:
            node.right = obj
        return obj
