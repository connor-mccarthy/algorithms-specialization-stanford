from typing import Tuple


def int_length(integer: int) -> int:
    return len(str(integer))


def split_int(integer: int, idx: int) -> Tuple[int, int]:
    return integer // 10 ** (idx), integer % 10 ** (idx)


def karatsuba(int1: int, int2: int) -> int:
    if (int_length(int1) == 1) or (int_length(int2) == 1):
        return int1 * int2

    n = int_length(int1)
    split_idx = n // 2

    a, b = split_int(int1, split_idx)
    c, d = split_int(int2, split_idx)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    gauss_intermediate = karatsuba((a + b), (c + d))
    ad_plus_bc = gauss_intermediate - ac - bd

    return (
        ((10 ** (2 * split_idx)) * ac) + ((10 ** (split_idx)) * ad_plus_bc) + bd
    )  # doesn't need to use karatsuba because will only improve lower order terms


print(
    karatsuba(
        3141592653589793238462643383279502884197169399375105820974944592,
        2718281828459045235360287471352662497757247093699959574966967627,
    )
)
