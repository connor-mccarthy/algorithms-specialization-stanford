from typing import List, Tuple

Array = List[int]
Result = List[Tuple[int, int]]


def brute_force(array: Array, t: int) -> Result:
    result = []
    for i, e1 in enumerate(array):
        for e2 in array[i + 1 :]:
            if e1 + e2 == t:
                result.append((e1, e2))
    return result


def sorted_array(array: Array, t: int) -> Result:
    array = sorted(array)
    result = []
    for i, e1 in enumerate(array):
        for e2 in array[i + 1 :]:
            if e1 + e2 == t:
                result.append((e1, e2))
    return result


def create_hash_table_from_array(array: Array) -> List[bool]:
    min_key = 10000
    max_key = 10000
    hash_table = [False for _ in range(-min_key, max_key + 1)]
    for e in array:
        hash_table[e + min_key] = True
    return hash_table


def hash_table_2_sum(array: Array, t: int) -> Result:
    hash_table = create_hash_table_from_array(array)
    return [(e, t - e) for e in array if hash_table[t - e]]
