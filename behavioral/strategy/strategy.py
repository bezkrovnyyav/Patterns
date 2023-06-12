from abc import ABC, abstractmethod
from enum import Enum


class BaristaMood(Enum):
    """Barista`s mood"""
    GOOD = 1
    BAD = 2


class Strategy(ABC):
    """Strategy Interface"""

    @abstractmethod
    def check_mood_barista(self, mood: BaristaMood) -> bool:
        ...

    @abstractmethod
    def order_processing(self, money: int) -> str:
        ...


class GoodStrategy(Strategy):

    def check_mood_barista(self, mood: BaristaMood) -> bool:
        if (mood is BaristaMood.GOOD or mood is BaristaMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return "The best coffee is created!"


class BadStrategy(Strategy):

    def check_mood_barista(self, mood: BaristaMood) -> bool:
        if (mood is BaristaMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return "Create bad coffee"


class OptimalStrategy(Strategy):

    def check_mood_barista(self, mood: BaristaMood) -> bool:
        # maybe the barista has bad mood, but customers are not guilty
        return True

    def order_processing(self, money: int) -> str:
        if money < 5:
            return "Do not serve the customer"
        elif money < 10:
            return "Create espresso"
        elif money < 20:
            return "Create cappuccino"
        elif money < 50:
            return "Create the best coffee"
        else:
            return "Create the best coffee possible!"


class Barista:
    def __init__(self, strategy: Strategy,
                 barista_mood: BaristaMood):
        self._strategy = strategy
        self._barista_mood = barista_mood
        print(f"Base barista`s mood: {barista_mood.name}")

    def get_barista_mood(self) -> BaristaMood:
        return self._barista_mood

    def set_barista_mood(self, barista_mood: BaristaMood) -> None:
        print(f"Barista`s current mood: {barista_mood.name}")
        self._barista_mood = barista_mood

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, money: int) -> None:
        print(f"Client give {money} money", self._barista_mood)
        if self._strategy.check_mood_barista(self._barista_mood):
            print(self._strategy.order_processing(money))
        else:
            print("Do not serve the client")


if __name__ == "__main__":
    barista = Barista(OptimalStrategy(), BaristaMood.GOOD)
    barista.take_order(19)
    barista.take_order(50)
    barista.set_strategy(BadStrategy())
    barista.take_order(40)
    barista.take_order(100)
    barista.set_strategy(GoodStrategy())
    barista.set_barista_mood(BaristaMood.GOOD)
    barista.take_order(0)