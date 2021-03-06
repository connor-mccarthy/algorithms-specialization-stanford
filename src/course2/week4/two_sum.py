from typing import Dict, List, Tuple

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


def create_hash_table_from_array(array: Array) -> Dict[int, bool]:
    # python dictionaries are stored by the hash value of the key for fast lookup
    hash_table: Dict[int, bool] = {}
    for e in array:
        hash_table[e] = True
    return hash_table


def hash_table_2_sum(array: Array, t: int) -> Result:
    hash_table = create_hash_table_from_array(array)
    return [(e, t - e) for e in array if hash_table.get(t - e, False) and t - e != e]
