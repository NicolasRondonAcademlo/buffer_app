from app.utils import BufferAbstract, NoDataInBuffer, Node


class BufferFiFo(BufferAbstract):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def insert(self, data):
        """
        Insert ane element in Buffer
        :param data: Element to insert
        :return: None
        """
        new_node = Node(data, None, None)

        if self.__head is None:
            self.__head = new_node
            self.__tail = self.__head
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    def extract(self):
        """
        Remo element from Buffer
        :return: First Element in Buffer
        """
        if not self.count:
            raise NoDataInBuffer("No hay elementos en Buffer")
        current = self.__head
        if self.__count == 1:
            self.__count -= 1
            self.__head = None
            self.__tail = None
        elif self.__count > 1:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__count -= 1
        if current.data:
            return current.data
        else:
            return None


class BufferLiFo(BufferAbstract):
    def __init__(self) -> None:
        self.__top = None
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def insert(self, data):
        node = Node(data)
        if self.__top:
            node.next = self.__top
            self.__top = node
        else:
            self.__top = node
        self.__count += 1

    def extract(self):
        if not self.count:
            raise NoDataInBuffer("No hay elementos en Buffer")
        if self.__top:
            data = self.__top.data
            self.__count -= 1
            if self.__top.next:
                self.__top = self.__top.next
            else:
                self.__top = None
            return data
        else:
            return None


mapper = {"FIFO": BufferFiFo, "LIFO": BufferLiFo}


def buffer_factory(policy: str):
    buffer = mapper.get(policy)
    return buffer()
