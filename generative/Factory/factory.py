from enum import Enum


class CoffeeType(Enum):
    """
    This coffee we can created
    """
    CAPPUCCINO  = 0,
    AMERICANO = 1,
    ESPRESSO = 2


class Coffee:
    """
    Base classes coffee for creation next classes
    """
    def __init__(self, price: float):
        self.__price = price # coffee price

    def get_price(self) -> float:
        return self.__price


class Cappuccino(Coffee):
    def __init__(self):
        super().__init__(30)


class Americano(Coffee):
    def __init__(self):
        super().__init__(40)


class Espresso(Coffee):
    def __init__(self):
        super().__init__(50)


def create_coffee(coffee_type: CoffeeType) -> Coffee:
    """
    This is Factory Method
    """
    factory_dict = {
        CoffeeType.CAPPUCCINO : Cappuccino,
        CoffeeType.AMERICANO: Americano,
        CoffeeType.ESPRESSO: Espresso
    }
    return factory_dict[coffee_type]()


if __name__ == '__main__':
    for coffee in CoffeeType:
        my_coffee = create_coffee(coffee)
        print(f'Coffee type: {coffee}, price: {my_coffee.get_price()}')
