from abc import ABC, abstractmethod
"""transfers the implementation of tasks sequentially"""


class BaseWorker(ABC):

    @abstractmethod
    def set_next_worker(self, worker: 'BaseWorker') -> 'BaseWorker':
        pass


    @abstractmethod
    def execute(self, command: str) -> str:
        pass


class AbsWorker(BaseWorker):

    def __init__(self):
        self.__next_worker : BaseWorker = None


    def set_next_worker(self, worker: 'BaseWorker') -> 'BaseWorker':
        self.__next_worker = worker
        return worker


    def execute(self, command: str) -> str:
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)

        return ''


class Designer(AbsWorker):

    def execute(self, command: str) -> str:
        if command == 'design a house':
            return 'the designer executed the command:' + command
        return super().execute(command)



class Carpenters(AbsWorker):

    def execute(self, command: str) -> str:
        if command == 'laying a brick':
            return 'the carpenter executed the command:' + command
        return super().execute(command)


class FinishingWorker(AbsWorker):

    def execute(self, command: str) -> str:
        if command == 'glue wallpaper':
            return 'the interior decoration worker executed the command:' + command
        return super().execute(command)


def client_command(worker: BaseWorker, command: str):
    string : str = worker.execute(command)
    if string == '':
        print(command + '- no one knows how to do it')
    else:
        print(string)


if __name__ == '__main__':

    designer = Designer()
    carpenters = Carpenters()
    finishing_worker = FinishingWorker()

    designer.set_next_worker(carpenters).set_next_worker(finishing_worker)

    client_command(designer, 'design a house')
    client_command(designer, 'laying a brick')
    client_command(designer, 'glue wallpaper')

    client_command(designer, 'create electrisity system ')
