import pandas as pd
import unittest
from util import get_easter

df = pd.read_csv('ortodox-easter-1800-2026.csv')

class TestCalc(unittest.TestCase):

    def test_easter(self):
        """Test the add function with basic inputs."""
        i = 0
        for i in range(0, len(df)):
            row = df.iloc[1]
            y = row['year']
            m = row['month']
            d = row['day']
            e = get_easter(y)
            self.assertEqual(e.month, m)
            self.assertEqual(e.day, d)

if __name__ == '__main__':
    unittest.main()
