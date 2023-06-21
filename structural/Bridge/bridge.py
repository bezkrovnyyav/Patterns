from abc import ABC, abstractmethod
"""abstraction and implementation"""


class BaseDataReader(ABC):
    """
    Abstract for creating data source
    """

    @abstractmethod
    def read(self):
        pass


class DataBaseReader(BaseDataReader):
    """
    For database operations
    """

    def read(self):
        print("data from the database ", end='')


class FileReader(BaseDataReader):
    """
    For oparation with data from file
    """

    def read(self):
        print("data from the file ", end='')


class BaseSender(ABC):
    """
    For send info to the user
    """

    def __init__(self, data_reader: BaseDataReader):
        self.reader: BaseDataReader = data_reader

    def set_data_reader(self, data_reader: BaseDataReader):
        self.reader: BaseDataReader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(BaseSender):
    """
    Send data via email
    """

    def __init__(self, data_reader: BaseDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print("sent by email")


class TelegramBotSender(BaseSender):
    """
    Send data to Telegram
    """

    def __init__(self, data_reader: BaseDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print("sent by telegram bot")


if __name__ == '__main__':

    sender = TelegramBotSender(DataBaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender: BaseSender = EmailSender(DataBaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()
