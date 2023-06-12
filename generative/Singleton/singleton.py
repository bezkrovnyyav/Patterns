class SingletonClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cafe(metaclass=SingletonClass):
    def __init__(self):
        self.name = "Coffee"
        self.milk = " and Milk"

    def add_milk(self) -> int:
        return self.name + self.milk

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


if __name__ == "__main__":
    cafe_1 = Cafe()
    cafe_2 = Cafe()
    print("Singleton1 name: " + cafe_1.get_name())
    cafe_1.set_name("My new coffee")
    print("Singleton2 name: " + cafe_2.get_name())
    print("Singleton1 add milk: ", cafe_1.add_milk())
    print(cafe_1)
    print(cafe_2)
    print(id(cafe_1) == id(cafe_2))
