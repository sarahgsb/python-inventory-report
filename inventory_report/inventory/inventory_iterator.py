from collections.abc import Iterator


class InventoryIterator(Iterator):
    @classmethod
    def __init__(self, list):
        self.list = list
        self.index = 0

    def __next__(self):
        try:
            data = self.list[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return data
