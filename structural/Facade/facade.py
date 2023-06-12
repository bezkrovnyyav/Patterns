class ProviderCommunication:

    def receive(self):
        print('Receiving products from the manufacturer')

    def payment(self):
        print('Get payment')


class Site:

    def placement(self):
        print('Placement on the website')

    def delete(self):
        print('Removal from the site')


class Database:

    def insert(self):
        print('Writing to the database')

    def delete(self):
        print('Deleting from the database')


class MarketPlace:

    def __init__(self):
        self._provider_communication = ProviderCommunication()
        self._site = Site()
        self._database = Database()

    def product_receipt(self):
        self._provider_communication.receive()
        self._site.placement()
        self._database.insert()

    def product_release(self):
        self._provider_communication.payment()
        self._site.delete()
        self._database.delete()


if __name__ == '__main__':
    market_place = MarketPlace()
    market_place.product_receipt()
    print("-" * 20)
    market_place.product_release()
