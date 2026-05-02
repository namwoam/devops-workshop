"""
Unit tests for the linear algebra library.
This file contains test cases for practice. Most tests are left unimplemented.
"""

import unittest
import math
from lab1.lib import Vector, Matrix, create_identity_matrix, create_zero_matrix, create_zero_vector


class TestVector(unittest.TestCase):
    """Test cases for the Vector class."""
    
    def test_vector_creation(self):
        """Test creating a vector with components."""
        vec = Vector([1.0, 2.0, 3.0])
        self.assertEqual(len(vec), 3)
        self.assertEqual(vec[0], 1.0)
        self.assertEqual(vec[1], 2.0)
        self.assertEqual(vec[2], 3.0)
    
    def test_vector_addition(self):
        """Test vector addition."""
        pass  # TODO: Implement this test
    
    def test_vector_subtraction(self):
        """Test vector subtraction."""
        pass  # TODO: Implement this test
    
    def test_vector_scalar_multiplication(self):
        """Test vector scalar multiplication."""
        pass  # TODO: Implement this test
    
    def test_vector_magnitude(self):
        """Test calculating vector magnitude."""
        pass  # TODO: Implement this test
    
    def test_vector_dot_product(self):
        """Test dot product between two vectors."""
        pass  # TODO: Implement this test
    
    def test_vector_normalization(self):
        """Test normalizing a vector to unit length."""
        pass  # TODO: Implement this test
    
    def test_vector_distance(self):
        """Test Euclidean distance between two vectors."""
        pass  # TODO: Implement this test
    
    def test_vector_dimension_mismatch(self):
        """Test that operations with mismatched dimensions raise errors."""
        pass  # TODO: Implement this test
    
    def test_vector_equality(self):
        """Test vector equality comparison."""
        pass  # TODO: Implement this test


class TestMatrix(unittest.TestCase):
    """Test cases for the Matrix class."""
    
    def test_matrix_creation(self):
        """Test creating a matrix."""
        pass  # TODO: Implement this test
    
    def test_matrix_addition(self):
        """Test matrix addition."""
        pass  # TODO: Implement this test
    
    def test_matrix_subtraction(self):
        """Test matrix subtraction."""
        pass  # TODO: Implement this test
    
    def test_matrix_scalar_multiplication(self):
        """Test matrix scalar multiplication."""
        pass  # TODO: Implement this test
    
    def test_matrix_multiplication(self):
        """Test matrix-to-matrix multiplication."""
        pass  # TODO: Implement this test
    
    def test_matrix_vector_multiplication(self):
        """Test matrix-vector multiplication."""
        pass  # TODO: Implement this test
    
    def test_matrix_transpose(self):
        """Test matrix transpose operation."""
        pass  # TODO: Implement this test
    
    def test_matrix_determinant_2x2(self):
        """Test determinant calculation for 2x2 matrix."""
        pass  # TODO: Implement this test
    
    def test_matrix_determinant_3x3(self):
        """Test determinant calculation for 3x3 matrix."""
        pass  # TODO: Implement this test
    
    def test_matrix_inverse_2x2(self):
        """Test inverse calculation for 2x2 matrix."""
        pass  # TODO: Implement this test
    
    def test_matrix_inverse_singular(self):
        """Test that singular matrices cannot be inverted."""
        pass  # TODO: Implement this test
    
    def test_matrix_trace(self):
        """Test trace calculation."""
        pass  # TODO: Implement this test
    
    def test_matrix_dimension_mismatch_addition(self):
        """Test that adding matrices with mismatched dimensions raises error."""
        pass  # TODO: Implement this test
    
    def test_matrix_dimension_mismatch_multiplication(self):
        """Test that multiplying incompatible matrices raises error."""
        pass  # TODO: Implement this test


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_create_identity_matrix(self):
        """Test creating an identity matrix."""
        pass  # TODO: Implement this test
    
    def test_create_zero_matrix(self):
        """Test creating a zero matrix."""
        pass  # TODO: Implement this test
    
    def test_create_zero_vector(self):
        """Test creating a zero vector."""
        pass  # TODO: Implement this test


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions."""
    
    def test_empty_vector_creation(self):
        """Test that creating empty vector raises error."""
        pass  # TODO: Implement this test
    
    def test_zero_vector_normalization(self):
        """Test that normalizing zero vector raises error."""
        pass  # TODO: Implement this test
    
    def test_divide_by_zero(self):
        """Test that division by zero raises error."""
        pass  # TODO: Implement this test
    
    def test_non_square_matrix_determinant(self):
        """Test that determinant of non-square matrix raises error."""
        pass  # TODO: Implement this test
    
    def test_non_square_matrix_inverse(self):
        """Test that inverse of non-square matrix raises error."""
        pass  # TODO: Implement this test


if __name__ == '__main__':
    unittest.main()
