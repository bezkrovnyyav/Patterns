from abc import ABC, abstractmethod


class Drink(ABC):

    @abstractmethod
    def drink(self):
        pass


class Tea(Drink):

    def drink(self):
        print('Nice tea  is created')


class Coffee(Drink):

    def drink(self):
        print('Nice coffee is created')


class DrinkFactory(ABC):

    @staticmethod
    @abstractmethod
    def prepare(amount: int):
        pass


class TeaFactory(DrinkFactory):

    @staticmethod
    def prepare(amount: int):
        """Object setting"""
        print('Boil water')
        print(f'Put into a cup {amount // 100} tsp. of tea leaves')
        print(f'Pour {amount} ml boiling water into a cup')
        return Tea()


class CoffeeFactory(DrinkFactory):

    @staticmethod
    def prepare(amount: int):
        """Object setting"""
        print(f'Put in the Turk {amount // 100} tsp. ground coffee')
        print(f'Pour {amount} ml of cold water into the cezve')
        print('Keep the coffee on low heat until it boils.')
        return Coffee()


def make_drink(kind: str):
    """Got the specified amount of a drink of the desired type."""
    if kind.lower() in ('tea'):
        return TeaFactory.prepare(200)
    elif kind.lower() in ('coffee'):
        return CoffeeFactory.prepare(300)
    else:
        return None

if __name__ == '__main__':
    choose_drink =  input('What do you like (tea or coffee)? ')
    prepare_drink = make_drink(choose_drink)
    prepare_drink.drink()
