from abc import ABC, abstractmethod
from typing import List
"""add new operations without changing object classes"""


class BaseVisitor(ABC):

    @abstractmethod
    def visit(self, place: 'BasePlace'):
        pass


class BasePlace(ABC):

    @abstractmethod
    def accept(self, visitor: BaseVisitor):
        pass


class Cofe(BasePlace):

    def accept(self, visitor: BaseVisitor):
        visitor.visit(self)


class Cinema(BasePlace):

    def accept(self, visitor: BaseVisitor):
        visitor.visit(self)


class Theater(BasePlace):

    def accept(self, visitor: BaseVisitor):
        visitor.visit(self)


class HolidayMaker(BaseVisitor):

    def __init__(self):
        self.value = ''

    def visit(self, place: 'BasePlace'):
        if isinstance(place, Cofe):
            self.value = 'Cafe'
        elif isinstance(place, Cinema):
            self.value = 'Cinema'
        elif isinstance(place, Theater):
            self.value = 'Theater'


if __name__ == '__main__':

    places : List[BasePlace] = [Cofe(), Cinema(), Theater()]

    for places in places:
        visitor = HolidayMaker()
        places.accept(visitor)
        print(visitor.value)
