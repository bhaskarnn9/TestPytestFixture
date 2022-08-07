import pytest


@pytest.fixture(autouse=True)
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    print('\n running auto fixture')
    # order = ['a']
    return order.append(first_entry)


def test_string_only(order, first_entry):

    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]


def test_last(order, first_entry):
    order.append(2)
    order.append(1)
    assert order == [first_entry, 2, 1]
