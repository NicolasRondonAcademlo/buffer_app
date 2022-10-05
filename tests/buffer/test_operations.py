import pytest

from app.buffer import Buffer
from app.utils import NoDataInBuffer

operations_mapper = {"lifo": 5, "fifo": 1}


@pytest.mark.parametrize("operation, response", operations_mapper.items())
def test_buffer_operations(operation, response):

    buffer = Buffer(operation)
    buffer.insert(1)
    buffer.insert(2)
    buffer.insert(3)
    buffer.insert(4)
    buffer.insert(5)

    assert response == buffer.extract()


def test_policy_incorrect():
    try:
        Buffer("TIFO")
        assert False
    except ValueError:
        assert True


@pytest.mark.parametrize("operation, response", operations_mapper.items())
def test_buffer_count(operation, response):

    buffer = Buffer(operation)
    buffer.insert(1)
    buffer.insert(2)
    buffer.insert(3)
    buffer.insert(4)
    buffer.insert(5)

    assert buffer.count == 5


@pytest.mark.parametrize("operation, response", operations_mapper.items())
def test_no_items_in_buffer(operation, response):
    try:
        buffer = Buffer(operation)
        buffer.extract()
        assert False
    except NoDataInBuffer:
        assert True


# value = Buffer("FIFO")
#
# value.insert(1)
# value.insert(2)
# value.insert(3)
# value.insert(4)
# print(value.extract())
# print(value.extract())
# print(value.count)
#
# print("---*--")
# value = Buffer("LIFO")
#
# value.insert(1)
# value.insert(2)
# value.insert(3)
# value.insert(4)
# print(value.extract())
# print(value.extract())
# print(value.count)
