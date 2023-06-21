from collections.abc import Iterable, Iterator
from  typing import Any
"""iterates over elements"""


class AlphabeticalOrderIterator(Iterator):
    _position: int = None # stores the current traversal position
    _reverse: bool = False # indicates the direction of traversal.

    def __init__(self, collection: 'WordsCollection', *, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        method is used in iterator and should return the next element in the iterable object
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    def __init__(self, collection: list[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        method is used in iterable object (list) 
        and returns an iterator object sorted in ascending order.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        """
        reverses the iterable's traversal direction
        """
        return AlphabeticalOrderIterator(self._collection, reverse=True)

    def add(self, item: Any):
        self._collection.append(item)


if __name__ == '__main__':
    words_collection = WordsCollection()
    words_collection.add('First')
    words_collection.add("Second")
    words_collection.add("Third")

    print('\n'.join(words_collection))
    print('\n'.join(words_collection.get_reverse_iterator()))
