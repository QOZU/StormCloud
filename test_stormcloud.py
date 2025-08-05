# test_stormcloud.py
"""
Tests for StormCloud module.
"""

import unittest
from stormcloud import StormCloud

class TestStormCloud(unittest.TestCase):
    """Test cases for StormCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StormCloud()
        self.assertIsInstance(instance, StormCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StormCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
