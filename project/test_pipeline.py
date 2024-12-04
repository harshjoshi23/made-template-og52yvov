
import unittest
import os

# Import the main function from pipeline script
from pipeline import main

class TestDataPipeline(unittest.TestCase):
    def test_output_existence(self):
        """Test to check if the output database file exists."""
        main()  
        # Cpath check 
        self.assertTrue(os.path.exists('../data/covid_data.sqlite'), "Output database does not exist.")

if __name__ == '__main__':
    unittest.main()
