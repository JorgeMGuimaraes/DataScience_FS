#region imports
from typing import List, Tuple, Callable
import math
#EndRegion
#Region types
Vector = List[float]
Matrix = List[List[float]]
#endregion
#region definitions
def add(v: Vector, w: Vector):
    """Add corresponding elements"""
    assert len(v) == len(w), "Vectors must be of same length"
    return [vi + wi for vi, wi in zip(v, w)]

def subtract(v: Vector, w: Vector):
    """Subtract corresponding elements"""
    assert len(v) == len(w), "Vectors must be of same length"
    return [vi - wi for vi, wi in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    assert vectors, "No vectors provided."
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Vectors have different sizes"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Scalar multiplication: multiply every element of _v_ by _c_"""
    return [c * vi for vi in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Compute the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))

def dot_product(v: Vector, w: Vector) -> float:
    """Computes v1 * w1 + vn * wn"""
    assert len(v) == len(w), "Vectors must be of the same length"
    return sum(vi * wi for vi, wi in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    """Returns v1 * v1 + ... + vn * vn """
    return dot_product(v, v)

def magnitude(v: Vector) -> float:
    """Returns the Euclidean legnth (norm) of v"""
    return math.sqrt(sum_of_squares(v))

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns the number of rows, number of columns of A"""
    num_rows    = len(A)
    num_columns = len(A[0]) if A else 0
    return num_rows, num_columns

def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row (Vector) of A"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column (Vector) of A"""
    return [Ai[j] for Ai in A]

def make_matrix(num_rows: int, num_cols: int, entry_function_N: Callable[[int, int], float]) -> Matrix:
    """Returns Matrix rows x cols whose (i, j)-th element is defined as entry_function_N(i, j)"""
    return [[entry_function_N(i, j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """ Returns identity Matrix n x n"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
#endregion