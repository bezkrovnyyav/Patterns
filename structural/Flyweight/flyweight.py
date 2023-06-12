class CoffeeOrderFlyWeight:

    def __init__(self, shared_state):
        self.shared_state = shared_state

    def __str__(self):
        return str(self.shared_state)


class CoffeeOrderContext:

    def __init__(self, unique_state, flyweight: CoffeeOrderFlyWeight):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __str__(self):
        return f"unique state: {self.unique_state} \n" \
               f"split state: {self.flyweight}"


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state) -> CoffeeOrderFlyWeight:

        flyweights = list(filter(lambda x: x.shared_state ==
                                           shared_state, self.flyweights))
        if flyweights:
            return flyweights[0]
        else:
            flyweight = CoffeeOrderFlyWeight(shared_state)
            self.flyweights.append(flyweight)
            return flyweight

    @property
    def total(self):
        return len(self.flyweights)


class CoffeeOrderMaker:

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.contexts = []

    def make_coffee_order(self, unique_state, shared_state) -> CoffeeOrderContext:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = CoffeeOrderContext(unique_state, flyweight)
        self.contexts.append(context)

        return context


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory()
    coffee_maker = CoffeeOrderMaker(flyweight_factory)

    shared_states = [(50, 'Big portion'),
                     (25, 'Normal portion')]
    unique_states = ['Americano', 'Latte']

    orders = [coffee_maker.make_coffee_order(unique_state, shared_state)
              for unique_state in unique_states
              for shared_state in shared_states]

    print("Number of cups coffee created: ", len(orders))
    print("Number of separated objects: ", flyweight_factory.total)
    for coffee_id, coffee_info in enumerate(orders):
        print("-"*20)
        print(f"The number of the cup coffee in the list: {coffee_id}")
        print(coffee_info)
