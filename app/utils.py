from abc import ABC, abstractmethod


class BufferAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def insert(self, data) -> None:
        pass

    @abstractmethod
    def extract(self) -> None:
        pass


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class NoDataInBuffer(Exception):
    pass
