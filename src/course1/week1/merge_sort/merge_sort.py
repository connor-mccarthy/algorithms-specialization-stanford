from typing import List, Tuple


def split_array(array: List[int]) -> Tuple[List[int], List[int]]:
    split_idx = len(array) // 2
    return array[:split_idx], array[split_idx:]


def merge(a: List[int], b: List[int]) -> List[int]:
    i = 0
    j = 0
    output = []
    for _ in range(len(a + b)):
        if i == len(a):  # handle cases where fall off a
            output.append(b[j])
            j += 1
        elif j == len(b):  # handle cases where fall off b
            output.append(a[i])
            i += 1
        elif a[i] < b[j]:  # main merge procedure
            output.append(a[i])
            i += 1
        elif b[j] < a[i]:  # main merge procedure
            output.append(b[j])
            j += 1
        elif a[i] == b[j]:  # handle same elements
            output.append(a[i])  # the first "if" will catch the corresponding b element
            i += 1
    return output


def merge_sort(array: List[int]) -> List[int]:
    if len(array) in [0, 1]:  # base case
        return array

    a, b = split_array(array)
    a_sorted = merge_sort(a)
    b_sorted = merge_sort(b)
    return merge(a_sorted, b_sorted)
