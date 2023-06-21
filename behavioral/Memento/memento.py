from typing import List
"""save base and restore past states of objects"""


class Memento:
    """Is captured the current state of presence of ingredients in coffee"""

    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Coffee:
    """Create coffee via barista"""
    def __init__(self):
        self.__state: List[str] = ['base_coffee']

    def add_ingredient(self, ingredient: str) -> None:
        print(f"Ingredient added to coffee: {ingredient}")
        self.__state.append(ingredient)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f"Base state of the coffee: {self.__state}"


class Barista:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        self.coffee_states: List[Memento] = []

    def add_ingredient_to_coffee(self, ingredient: str):
        self.coffee_states.append(self.coffee.create_memento())
        self.coffee.add_ingredient(ingredient)


    def undo_add_ingredient(self):
        if len(self.coffee_states) == 1:
            self.coffee.set_memento(self.coffee_states[0])
            print("Coffee returned to base state")
            print(self.coffee)
        else:
            print("Reject a previous action")
            state = self.coffee_states.pop()
            self.coffee.set_memento(state)
            print(self.coffee)


if __name__ == "__main__":
    coffee = Coffee()
    barista = Barista(coffee)
    print(coffee)
    print("*" * 8 + "Add ingredients into the coffee" + 8 * "*")
    barista.add_ingredient_to_coffee('water')
    barista.add_ingredient_to_coffee('sugar')
    barista.add_ingredient_to_coffee('milk')
    print(coffee)
    print("*" * 4 + "Reject previous actions" + 4 * "*")
    barista.undo_add_ingredient()
    barista.undo_add_ingredient()
    barista.undo_add_ingredient()
    print("*" * 5 + "Re-adding ingredients to coffee" + 5 * "*")
    barista.add_ingredient_to_coffee('water')
    barista.add_ingredient_to_coffee('syrup')
    print(coffee)
