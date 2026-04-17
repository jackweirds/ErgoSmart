# test_ergosmart.py
"""
Tests for ErgoSmart module.
"""

import unittest
from ergosmart import ErgoSmart

class TestErgoSmart(unittest.TestCase):
    """Test cases for ErgoSmart class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ErgoSmart()
        self.assertIsInstance(instance, ErgoSmart)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ErgoSmart()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
