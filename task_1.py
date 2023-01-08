
from collections import defaultdict

import numpy as np


def func(ar):
    a = np.median(ar)
    b = np.median(np.abs(ar - a))
    if np.isnan(b):
        msg = 'something is wrong'
        raise ValueError(msg)
    return b


class Thingy:
    def __init__(self):
        self._data = defaultdict(lambda: 0)

    def _func1(self, a):
        if isinstance(a, str):
            return [a]
        try:
            collection = iter(a)
        except TypeError:
            collection = [a]
        return collection

    def __call__(self, a):
        for x in self._func1(a):
            self._data[x] += 1

    def __str__(self):
        return str(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __getattr__(self, item):
        return self._data[item]

    def __iter__(self):
        return iter(self.data)

    def items(self):
        return self._data.items()

    def __len__(self):
        return len(self._data)
