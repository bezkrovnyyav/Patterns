from abc import ABCMeta, abstractmethod
from typing import  Any


class Builder(metaclass=ABCMeta):

    def __init__(self):
        self.reset()

    def reset(self) -> 'Coffee':
        self._product = Coffee()

    @property
    def product(self):
        return self._product

    @abstractmethod
    def add_first_ingredient(self):
        pass

    @abstractmethod
    def add_second_ingredient(self):
        pass

    @abstractmethod
    def add_third_ingredient(self):
        pass


class ConcreteBuilder1(Builder):

    def add_first_ingredient(self):
        self._product.add('Milk')
        return self

    def add_second_ingredient(self):
        self._product.add('Sugar')
        return self

    def add_third_ingredient(self):
        self._product.add('Ice cream')
        return self


class ConcreteBuilder2(Builder):

    def add_first_ingredient(self):
        self._product.add('Sugar')
        return self

    def add_second_ingredient(self):
        self._product.add('Cream')
        return self

    def add_third_ingredient(self):
        self._product.add('Caramel syrup')
        return self


class Coffee:
    def __init__(self):
        self._parts = []

    def add(self, part: Any) -> None:
        self._parts.append(part)

    @property
    def parts(self):
        return f"Coffee with: {', '.join(self._parts)}"


class Director:
    def __init__(self, builder: Builder):
        self.__builder = builder

    def build_first_obj(self):
        return self.__builder.add_first_ingredient().add_second_ingredient()

    def build_second_obj(self):
        return self.__builder.add_second_ingredient().add_third_ingredient()


if __name__ == '__main__':
    builder1 = ConcreteBuilder1()
    director = Director(builder1)
    director.build_first_obj()
    print(builder1.product.parts)

    builder2 = ConcreteBuilder2()
    director = Director(builder2)
    director.build_second_obj()
    print(builder2.product.parts)
