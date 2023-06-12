from abc import ABC, abstractmethod


class BaseScale(ABC):
    """
    Abstract class of the Scales System for Adapter  
    """

    @abstractmethod
    def get_weight(self) -> float:
        pass


class EuropeanScales(BaseScale):
    """
    Implementation of the American Scales System    
    """

    def __init__(self, current_weight: float):
        self.__current_weight = current_weight

    def get_weight(self) -> float:
        return self.__current_weight


class AmericanScales:
    """
    Implementation of the American Scales System    
    """

    def __init__(self, current_weight: float):
        self.__current_weight = current_weight

    def get_weight(self) -> float:
        return self.__current_weight


class AdapterForAmericanScales(BaseScale):

    def __init__(self, american_scales: AmericanScales):
        self.__american_scales = american_scales

    def get_weight(self) -> float:
        return self.__american_scales.get_weight() * .453


if __name__ == '__main__':
    lb: float = 100
    american_scales = AdapterForAmericanScales(AmericanScales(lb))

    print(f"{lb} lb equal to {american_scales.get_weight()} kg")
