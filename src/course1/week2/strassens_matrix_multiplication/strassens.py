from typing import Tuple

import numpy as np


def split_matrix(
    matrix: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rows, cols = matrix.shape
    split_row, split_col = rows // 2, cols // 2
    return (
        matrix[:split_row, :split_col],
        matrix[:split_row, split_col:],
        matrix[split_row:, :split_col],
        matrix[split_row:, split_col:],
    )


def is_base_case(matrix: np.ndarray) -> bool:
    return len(matrix) == 1


def strassens(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    """O(n**log_2(7) == O(n**2.81)"""
    assert matrix1.shape[0] == matrix1.shape[1]
    assert matrix1.shape == matrix2.shape

    if is_base_case(matrix1):
        return matrix1 * matrix2

    a, b, c, d = split_matrix(matrix1)
    e, f, g, h = split_matrix(matrix2)

    p1 = strassens(a, f - h)
    p2 = strassens(a + b, h)
    p3 = strassens(c + d, e)
    p4 = strassens(d, g - e)
    p5 = strassens(a + d, e + h)
    p6 = strassens(b - d, g + h)
    p7 = strassens(a - c, e + f)

    v = p5 + p4 - p2 + p6
    x = p1 + p2
    y = p3 + p4
    z = p1 + p5 - p3 - p7

    top, bottom = np.hstack((v, x)), np.hstack((y, z))
    return np.vstack((top, bottom))
