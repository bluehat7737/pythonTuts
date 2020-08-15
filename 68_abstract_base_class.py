from abc import ABC, abstractmethod

# metaclass=ABCMeta
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rect(Shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rect()

print(rect1.printarea())