import sys

import pytest

sys.path.append(".")

from autodropstack import AutoDropStack


def test_initialize():
    s = AutoDropStack(5)
    assert len(s.stack) == 0


def test_push_integer():
    s = AutoDropStack(5)
    s.push(1)
    assert len(s.stack) == 1
    assert s.stack[0] == 1


def test_push_string():
    s = AutoDropStack(5)
    s.push("Hello World")
    assert len(s.stack) == 1
    assert s.stack[0] == "Hello World"


def test_overflow():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    assert len(s.stack) == 5
    assert s.stack[0] == 2
    assert s.stack[1] == 3
    assert s.stack[2] == 4
    assert s.stack[3] == 5
    assert s.stack[4] == 6


def test_percentiles():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    assert s.percentiles() == {2: 0.2, 3: 0.2, 4: 0.2, 5: 0.2, 6: 0.2}


def test_percentiles_unfilled():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.percentiles() == {
        1: 0.3333333333333333,
        2: 0.3333333333333333,
        3: 0.3333333333333333,
    }


def test_private_stack():
    s = AutoDropStack(5)
    with pytest.raises(AttributeError):
        s.__stack


def test_percentiles_empty_stack():
    s = AutoDropStack(5)
    assert s.percentiles() == {}


def test___str__():
    s = AutoDropStack(5)
    assert str(s) == "AutoDropStack(5)"


def test___repr__():
    s = AutoDropStack(5)
    assert repr(s) == "AutoDropStack(5)"


def test___len__():
    s = AutoDropStack(5)
    assert len(s) == 0
    s.push(1)
    assert len(s) == 1


def test___iter__():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    assert [i for i in s] == [1, 2, 3, 4, 5]


def test___getitem__():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    assert s[0] == 1
    assert s[1] == 2
    assert s[2] == 3
    assert s[3] == 4
    assert s[4] == 5


def test___setitem__():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s[0] = 10
    assert s[0] == 10
    assert s[1] == 2
    assert s[2] == 3
    assert s[3] == 4
    assert s[4] == 5


def test___delitem__():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    del s[0]
    assert s[0] == 2
    assert s[1] == 3
    assert s[2] == 4
    assert s[3] == 5


def test___contains__():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    assert 1 in s
    assert 2 in s
    assert 3 in s
    assert 4 in s
    assert 5 in s
    assert 6 not in s


def test___reversed__():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    assert [i for i in reversed(s)] == [5, 4, 3, 2, 1]
