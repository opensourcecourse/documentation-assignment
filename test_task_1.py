"""
Tests for task 2.
"""
import numpy as np
import pytest

from task_2 import Thingy, func


class TestFunc:

    def test_1(self):
        ar = np.ones(10)
        assert func(ar) == 0

    def test_2(self):
        ar = np.ones(10)
        ar[0] = np.NaN
        with pytest.raises(ValueError):
            func(ar)


class TestThingy:

    def test_1(self):
        thingy = Thingy()
        assert len(thingy) == 0
        inputs = [1, 2, 3]
        thingy(inputs)
        assert len(thingy) == len(inputs)
        thingy(inputs)
        assert len(thingy) == len(inputs)

    def test_2(self):
        inputs = (1, 2, 3)
        thingy = Thingy()
        thingy(inputs)
        for val in inputs:
            assert thingy[val] == 1
        thingy(inputs)
        for val in inputs:
            assert thingy[val] == 2

    def test_3(self):
        thing = Thingy()
        assert isinstance(str(thing), str)

    def test_4(self):
        thingy = Thingy()
        thingy('bob')
        assert thingy['bob'] == 1
