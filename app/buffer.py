from app.buffer_operations import buffer_factory


class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """

    def __init__(self, policy):
        policy = policy.upper()
        self.data = []
        if policy not in ["FIFO", "LIFO"]:
            raise ValueError()
        self.__policy = policy
        self.__buffer_client = buffer_factory(self.__policy)

    def insert(self, item):
        self.__buffer_client.insert(item)

    def extract(self):
        return self.__buffer_client.extract()

    @property
    def count(self):
        return self.__buffer_client.count
