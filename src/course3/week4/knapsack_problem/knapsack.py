from dataclasses import dataclass
from typing import List, Set

import numpy as np


@dataclass
class Item:
    value: int
    size: int


np.set_printoptions(formatter={"float": lambda x: "{0:0.3f}".format(x)})  # type: ignore


def construct_array(items: List[Item], capacity: int) -> np.ndarray:
    n_items = len(items)
    array = np.zeros((n_items + 1, capacity + 1))

    for i, item in enumerate(items, start=1):
        for cap in range(capacity + 1):
            if item.size > cap:
                array[i][cap] = array[i - 1][cap]
            else:
                case1 = array[i - 1][cap]
                case2 = array[i - 1][cap - item.size] + item.value
                array[i][cap] = max(case1, case2)
    return array


def reconstruction(array: np.ndarray, items: List[Item], capacity: int) -> Set[int]:
    return_items = set()
    for i in range(len(items) - 1, -1, -1):
        condition1 = items[i].size <= capacity
        condition2 = (
            array[i - 1][capacity - items[i].size] + items[i].value
            >= array[i - 1][capacity]
        )
        if condition1 and condition2:
            return_items.add(i)
            capacity -= items[i].size
    return return_items


def knapsack(items: List[Item], capacity: int) -> Set[int]:
    array = construct_array(items, capacity)
    print(array)
    return reconstruction(array, items, capacity)
