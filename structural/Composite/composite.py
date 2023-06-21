from abc import ABC, abstractmethod
"""tree structure"""


class BaseCoffee(ABC):
    """
    Abstract class of the Product
    """
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class CoffeeProduct(BaseCoffee):
    """
    Class of Product
    """
    def __init__(self, name, cost):
        self._cost = cost
        self._name = name

    def cost(self):
        return self._cost

    def get_name(self):
        return self._name


class CoffeeProductComponent(BaseCoffee):
    """
    Class coffee`s components
    """
    def __init__(self, name):
        self._name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        return cost

    def get_name(self):
        return self._name

    def add_product(self, product: BaseCoffee):
        self.products.append(product)

    def remove_product(self, product: BaseCoffee):
        self.products.remove(product)

    def clear_product(self):
        self.products = []


class Coffee(CoffeeProductComponent):
    """
    Class of creation coffee
    """
    def __init__(self, name):
        super(Coffee, self).__init__(name)

    def cost(self):
        cost = 0
        for product in self.products:
            coffee_cost = product.cost()
            print(f'Cost of {product.get_name()} = {coffee_cost}$')
            cost += coffee_cost
        print(f'Cost of coffee {self.get_name()} = {cost}$')
        return cost


if __name__ == '__main__':
    base_coffee = CoffeeProductComponent('Base coffee')
    base_coffee.add_product(CoffeeProduct('coffee', 4))
    base_coffee.add_product(CoffeeProduct('sugar', 3))
    base_coffee.add_product(CoffeeProduct('milk', 2))

    topping = CoffeeProductComponent('Cappuccino')
    topping.add_product(CoffeeProduct('coffee', 5))
    topping.add_product(CoffeeProduct('sugar', 4))
    topping.add_product(CoffeeProduct('milk', 6))
    moccoffee = Coffee('Mocaccino')

    moccoffee.add_product(base_coffee)
    moccoffee.add_product(topping)
    print(f'Mocaccino cost is {moccoffee.cost()}$')
