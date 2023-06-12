from abc import ABC, abstractmethod


class InterfaceCoffeeBase(ABC):
    """Declared object interface"""
    @abstractmethod
    def cost(self) -> float:
        pass


class CoffeeBase(InterfaceCoffeeBase):
    """Class of the decorated object """
    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost


class InterfaceDecorator(InterfaceCoffeeBase):
    """interface of decorator"""
    @abstractmethod
    def name(self) -> str:
        pass


class Americano(InterfaceDecorator):
    """Get Americano via CoffeeBase """
    def __init__(self, wrapped: InterfaceCoffeeBase, coffee_cost: float):
        self.__wrapped = wrapped
        self.__cost = coffee_cost
        self.__name = "Americano"

    def cost(self) -> float:
        return self.__cost+self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


class Cappuccino(InterfaceDecorator):
    """Get Cappuccino via CoffeeBase"""
    def __init__(self, wrapped: InterfaceCoffeeBase, coffee_cost: float):
        self.__wrapped = wrapped
        self.__cost = coffee_cost
        self.__name = "Cappuccino"

    def cost(self) -> float:
        return (self.__cost+self.__wrapped.cost()) * 1.5

    def name(self) -> str:
        return self.__name


if __name__ == "__main__":
    def print_coffee(coffee: InterfaceDecorator) -> None:
        print(f"Coffee cost '{coffee.name()}' = {coffee.cost()}")

    coffee_base = CoffeeBase(20)
    print(f"Base Coffee cost = {coffee_base.cost()}")
    americano = Americano(coffee_base, 30)
    print_coffee(americano)
    cappuccino = Cappuccino(coffee_base, 40)
    print_coffee(cappuccino)