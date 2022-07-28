#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using
    matmul, and returns the result.
    """
    return numpy.matmul(m_a, m_b)
